from django.conf.urls import url, include

urlpatterns = [
    url(r'^statement/', include('statement.urls.en'), name='statement'),
    url(r'', include('main.urls.en'), name='main'),
]

