# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
from translator.views import *


class Sender(Dynamic_Base):

    def Attach_Image(self, image_path, image_name):

        img_data = open(BASE_DIR + image_path, 'rb').read()

        img = MIMEImage(img_data, 'png')
        img.add_header('Content-Id', '<{0}>'.format(image_name))
        img.add_header("Content-Disposition", "inline", filename=image_name)

        self.email.attach(img)

    def Send_Contact_Question(self, title, content, recipient):
        html_file = 'contact_question.html'
        reply_to = [recipient]
        recipient = [recipient, ROOT_EMAIL]
        self.Send_Email(title, content, recipient, html_file, reply_to)

    def Send_Email(self, title, content, recipient,
                   html_file, reply_to=None, pdf=None):

        self.content = content
        html = self.Render_HTML('sender/' + html_file)

        self.email = EmailMultiAlternatives(
            subject=title,
            body=html.content.decode(),
            from_email='Spa Sungate <sender@arbuz.team>',
            to=recipient,
            reply_to=reply_to
        )

        if pdf: self.email.attach(pdf['name'], pdf['file'], 'application/pdf')
        self.email.attach_alternative(html.content.decode(), 'text/html')
        self.Attach_Image('/_static/img/logo.png', 'logo')
        self.email.send()

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)
        self.email = None
