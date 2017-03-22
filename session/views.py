from inspect import getmembers, ismethod
from translator.views import *
from root.models import *


class Session_Controller:

    def Check_Session_Arbuz(self):

        if 'arbuz_navigation' not in self.request.session:
            self.request.session['arbuz_navigation'] = []

        if 'arbuz_url' not in self.request.session:
            self.request.session['arbuz_url'] = {}

        if 'arbuz_permissions' not in self.request.session:
            self.request.session['arbuz_permissions'] = ''

        if 'arbuz_app' not in self.request.session:
            self.request.session['arbuz_app'] = ''

    def Check_Session_Root(self):

        if 'root_login' not in self.request.session:
            self.request.session['root_login'] = False

        if 'root_social_media' not in self.request.session:
            self.request.session['root_social_media'] = \
                Social_Media.objects.all()

    def Check_Session_Translator(self):

        if 'translator_language' not in self.request.session:
            self.request.session['translator_language'] = 'EN'

        if 'translator_currency' not in self.request.session:
            self.request.session['translator_currency'] = 'EUR'

        Translator.Set_Subdomain_Language(self.request)
        Translator.Set_Currency(self.request)

    def Check_Session_Main(self):

        if 'main_content_tab' not in self.request.session:
            self.request.session['main_content_tab'] = ''

    def Check_Session(self):

        methods = getmembers(self, predicate=ismethod)
        methods = [method[0] for method in methods]

        for method in methods:
            if 'Check_Session_' in method:
                getattr(Session_Controller, method)(self)


    def __init__(self, request):
        self.request = request
        self.Check_Session()



def Check_Session(request):
    Session_Controller(request)