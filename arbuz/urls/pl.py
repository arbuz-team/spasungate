from django.conf.urls import url, include

urlpatterns = [
    url(r'^komunikat/', include('statement.urls.pl'), name='statement'),
    url(r'', include('main.urls.pl'), name='main'),
]

