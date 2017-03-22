# -*- coding: utf-8 -*-
from sender.views import *
from arbuz.views import *
from main.models import *
from main.forms import *


class Editable_Tab(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        pass

    def Manage_Form_Content_Tab(self):

        content_tab = Form_Content_Tab(
            self.request, self.request.POST)

        if content_tab.is_valid():

            if self.request.session['main_content_tab']:
                content = self.request.session['main_content_tab']

            else: content = content_tab.save(commit=False)

            content.tab_name = content_tab.cleaned_data['tab_name']
            content.header = content_tab.cleaned_data['header']
            content.paragraph = content_tab.cleaned_data['paragraph']
            content.language = self.request.session['translator_language']
            content.save()

            content.Save_Image(content_tab.cleaned_data['image'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'content_tab':
            return self.Manage_Form_Content_Tab()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Manage_Button(self):

        if self.request.POST['__button__'] == 'delete':
            Content_Tab.objects.get(pk=self.request.POST['value']).delete()

        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def New(request):
        return Editable_Tab(request, only_root=True).HTML

    @staticmethod
    def Edit(request, pk):
        request.session['main_content_tab'] = \
            Content_Tab.objects.get(pk=pk)

        return Editable_Tab(request, only_root=True).HTML

    @staticmethod
    def Delete(request):
        return Editable_Tab(request, only_root=True).HTML

    @staticmethod
    def Launch(request):
        pass



class Start(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('main/start.html')

    @staticmethod
    def Launch(request):
        return Start(request).HTML


class About(Editable_Tab):

    def Manage_Content_Ground(self):
        language = self.request.session['translator_language']
        self.content['content'] = Content_Tab.objects.filter(
            tab_name='about', language=language)

        return self.Render_HTML('main/about.html')

    @staticmethod
    def Launch(request):
        return About(request).HTML



class Contact(Editable_Tab):

    def Create_Titles(self):

        self.content['form_detail'] = [
            {
                'title':    Text(self.request, 81),
                'hidden':   'url',
            },
            {
                'title':    Text(self.request, 82),
                'hidden':   'product',
            },
            {
                'title':    Text(self.request, 83),
                'hidden':   'url product',
            },
        ]

    def Manage_Content_Ground(self):
        language = self.request.session['translator_language']
        self.content['form'] = Form_Email_Contact(self.request)
        self.content['content'] = Content_Tab.objects.filter(
            tab_name='contact', language=language)

        self.Create_Titles()
        return self.Render_HTML('main/contact.html', 'email_contact')

    def Manage_Form(self):

        self.Create_Titles()
        self.content['form'] = Form_Email_Contact(
            self.request, self.request.POST)

        if self.content['form'].is_valid():

            title = self.content['form'].cleaned_data['title']
            email = self.content['form'].cleaned_data['email']

            content = {
                'client':   self.content['form'].cleaned_data['client'],
                'question': self.content['form'].cleaned_data['message'],
                'product':  self.content['form'].cleaned_data['product'],
                'url':      self.content['form'].cleaned_data['url'],
            }

            Sender(self.request).Send_Contact_Question(title, content, email)

            return self.Render_HTML('main/contact.html', 'email_contact')
        return self.Render_HTML('main/contact.html', 'email_contact')

    @staticmethod
    def Launch(request):
        return Contact(request).HTML
