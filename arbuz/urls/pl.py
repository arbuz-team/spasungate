from django.conf.urls import url, include

urlpatterns = [
    url(r'^administrator/', include('root.urls.pl'), name='root'),
    url(r'^komunikat/', include('statement.urls.pl'), name='statement'),
    url(r'^ustawienia/', include('setting.urls.pl'), name='setting'),
    url(r'^nawigacja/', include('navigation.urls.pl'), name='navigation'),
    url(r'', include('main.urls.pl'), name='main'),
]

