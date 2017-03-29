from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('server.main.urls.pl'), name='main'),
]

