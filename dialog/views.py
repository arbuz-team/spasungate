from main.forms import *
from translator.views import *
from inspect import getmembers, ismethod


class Dialog(Dynamic_Base):

    def Get_POST_Variable(self, name):

        if name in self.request.POST:
            return self.request.POST[name]

        else: return ''

    def Generate_Content(self):

        self.content['additional'] = {
            'name':     self.Get_POST_Variable('additional_name'),
            'action':   self.Get_POST_Variable('additional_action'),
            'value':    self.Get_POST_Variable('additional_value'),
            'reload':   self.Get_POST_Variable('additional_reload'),
            'redirect': self.Get_POST_Variable('additional_redirect'),
            'url':      self.Get_POST_Variable('additional_url'),
            'event':    self.Get_POST_Variable('additional_event'),
        }

    def Render_Dialog(self, file_name, form_name = '',
                      authorization=False, only_root=False):

        if not authorization and not only_root:
            return self.Render_HTML(file_name, form_name)

        if authorization:
            if self.request.session['user_login']:
                return self.Render_HTML(file_name, form_name)

        if only_root:
            if self.request.session['root_login']:
                return self.Render_HTML(file_name, form_name)

        return self.Unauthorized_Access()

    def Get_Dialog_Name(self):
        return self.request.POST['dialog_name']

    @staticmethod
    def Apply_Message():
        return JsonResponse({'__form__': 'true'})

    def Unauthorized_Access(self):
        self.content['title'] = Text(self.request, 69)
        self.content['text'] = Text(self.request, 70)
        return self.Render_HTML('dialog/alert.html')

    def Manage(self):

        if self.apply:
            return self.Apply_Message()

        # content for buttons in dialogs
        self.Generate_Content()

        methods = getmembers(self, predicate=ismethod)
        methods = [method[0] for method in methods]
        dialog_name = self.Get_Dialog_Name()

        for method in methods:
            if dialog_name in method.lower():
                return getattr(self.__class__, method)(self)

    def __init__(self, request, app_name, apply=False):
        Dynamic_Base.__init__(self, request)
        self.parent_app_name= app_name
        self.apply = apply



class Dialog_Alert(Dialog):

    def Manage_Language(self):
        return self.Render_Dialog('dialog/language.html')

    def Manage_Icons(self):
        self.content['title'] = Text(self.request, 137)
        self.content['text'] = Text(self.request, 138)
        return self.Render_Dialog('dialog/alert.html')

    def __init__(self, request, app_name):
        Dialog.__init__(self, request, app_name)
        self.HTML = self.Manage()



class Dialog_Confirm(Dialog):

    def __init__(self, request, app_name):
        Dialog.__init__(self, request, app_name)
        self.HTML = self.Manage()



class Dialog_Prompt(Dialog):

    def Generate_Content(self):

        self.content['additional'] = {
            'reload': self.request.POST['additional_reload'],
            'redirect': self.request.POST['additional_redirect'],
            'event': self.request.POST['additional_event'],
        }


    def Manage_Content_Tab(self):

        content = self.Get_Session_Variable()
        initial = {
            'header':       content.header,
            'paragraph':    content.paragraph,
        }

        self.content['title'] = Text(self.request, 93)
        self.content['image'] = content.image
        self.content['form'] = Form_Content_Tab(self.request,
            self.Get_POST(), initial=initial)

        return self.Render_Dialog('dialog/prompt.html',
                                  'content_tab', only_root=True)


    def Get_POST(self):

        if self.not_valid:
            return self.request.POST

        return None

    def Get_Session_Variable(self):

        session_variable = '{0}_{1}'.format(
            self.parent_app_name, self.Get_Dialog_Name())

        if session_variable in self.request.session:
            if self.request.session[session_variable]:
                return self.request.session[session_variable]

        return None

    def Get_Dialog_Name(self):

        if '__form__' in self.request.POST:
            return self.request.POST['__form__']

        return self.request.POST['dialog_name']

    def __init__(self, request, app_name, apply=False, not_valid=False):
        Dialog.__init__(self, request, app_name, apply)
        self.not_valid = not_valid
        self.HTML = self.Manage()
