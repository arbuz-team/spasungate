from django.conf.urls import url
from server.main import views

urlpatterns = [
    url(r'^$', views.Start.Launch, name='main.start'),
]
