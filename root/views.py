from arbuz.views import *
from root.forms import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):

        self.content['apps'] = [
            {
                'name': Text(self.request, 24),
                'url': self.Get_Path('root.sign_out', current_language=True),
                'icon': '/_static/img/icons/128/dark/logout.png',
            },
            {
                'name': Text(self.request, 135),
                'url': self.Get_Path('root.social_media', current_language=True),
                'icon': '/_static/img/icons/128/dark/social_group.png',
            },
        ]

        return self.Render_HTML('arbuz/start_app.html')

    @staticmethod
    def Launch(request):
        return Start_App(request, only_root=True).HTML



class Sign_In(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Root_Login(self.request)
        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form_Login(self):

        self.content['form'] = \
            Form_Root_Login(self.request, self.request.POST)

        if self.content['form'].is_valid():
            self.request.session['root_login'] = True
            self.request.session['main_number_product_on_page'] = 9

            self.content['form'] = None  # message of correct
            return self.Render_HTML('root/sign_in.html')

        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'login':
            return self.Manage_Form_Login()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return Sign_In(request, other_value=other_value,
                       length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Sign_In(request).HTML



class Sign_Out(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.request.session['root_login'] = False
        self.request.session['main_number_product_on_page'] = 10
        return self.Render_HTML('root/sign_out.html')

    def Check_Authorization(self):

        if self.authorization:
            if self.request.session['root_login']:
                return True

        else: return True
        return False

    @staticmethod
    def Launch(request):
        return Sign_Out(request, only_root=True).HTML



class Social_Media_Manager(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['social_media'] = Social_Media.objects.all()
        return self.Render_HTML('root/social_media.html')

    def Manage_Form(self):

        pk = self.request.POST['__form__']
        url = self.request.POST['value']

        social = Social_Media.objects.get(pk=pk)
        social.url = url
        social.save()

        return JsonResponse({'__form__': 'true'})

    @staticmethod
    def Launch(request):
        return Social_Media_Manager(request, only_root=True).HTML
