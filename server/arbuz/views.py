from server.session.views import *
from abc import ABCMeta, abstractmethod


class Manager(Dynamic_Base):

    def Clear_Session(self, key_contain=''):
        Dynamic_Base.Clear_Session(self, key_contain)
        Check_Session(self.request)

    def Index_Clear_Session(self):
        Check_Session(self.request)

    def Manage_Index(self):

        self.Index_Clear_Session()

        # change website to other language
        lang_redirect = Translator.Get_Language_Redirect(self.request)
        if lang_redirect:
            return lang_redirect

        return render(self.request, 'index.html', {})

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)
        self.clear_session = False



class Dynamic_Event_Manager(Manager, metaclass=ABCMeta):

    def Initialize(self):

        Check_Session(self.request)
        if self.request.method == 'GET':
            return self.Manage_Index()

    def __init__(self, request,
                 error_method=None,
                 other_value={},
                 clear_session=False):

        Manager.__init__(self, request)
        self.error_method = error_method
        self.other_value = other_value
        self.clear_session = clear_session

        try:

            self.Timer_Start()
            self.HTML = self.Initialize()
            self.Display_Status()

            if not self.HTML:
                self.Display_Status(message='NOT HTML')

        except Exception as exception:

            self.Display_Status(message='INTERNAL')
            raise exception

    @staticmethod
    @abstractmethod
    def Launch(request):
        return Dynamic_Event_Manager(request)