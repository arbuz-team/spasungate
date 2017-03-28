from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.Start.Launch, name='main.start'),
]
