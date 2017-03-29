# -*- coding: utf-8 -*-
from server.arbuz.views import *


class Start(Dynamic_Event_Manager):

    def Manage_Index(self):
        return self.Render_HTML('main/start.html')

    @staticmethod
    def Launch(request):
        return Start(request).HTML
