from django.contrib.gis.geoip import GeoIP
from django.shortcuts import redirect
from arbuz.base import *


class Translator:

    @staticmethod
    def Set_Subdomain_Language(request):

        url = request.get_host()
        subdomain = url.split('.')[0]

        if subdomain in ['pl', 'de', 'en']:
            request.session['translator_language'] = subdomain.upper()

    @staticmethod
    def Get_Language_Redirect(request):

        url = request.get_host()
        subdomain = url.split('.')[0]

        if subdomain not in ['pl', 'de', 'en']:
            client_ip = request.META.get('REMOTE_ADDR', None)

            geo = GeoIP()
            country = geo.country_code(client_ip)
            dynamic_base = Dynamic_Base(request)

            if country == 'PL':
                return redirect(dynamic_base.Get_Urls(language='PL'))

            if country == 'DE':
                return redirect(dynamic_base.Get_Urls(language='DE'))

        return None
