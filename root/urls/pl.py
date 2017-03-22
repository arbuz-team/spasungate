from django.conf.urls import url
from root import views

urlpatterns = [
    url(r'^$', views.Start_App.Launch, name='root.start'),
    url(r'^zaloguj/$', views.Sign_In.Launch, name='root.sign_in'),
    url(r'^wyloguj/$', views.Sign_Out.Launch, name='root.sign_out'),
    url(r'^media_spolecznosciowe/$', views.Social_Media_Manager.Launch, name='root.social_media'),

    url(r'^sign_in/redirect/(?P<url>.+)/$',
        views.Sign_In.Redirect, name='root.sign_in.redirect'),
]

