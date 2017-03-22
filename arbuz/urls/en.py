from django.conf.urls import url, include

urlpatterns = [
    url(r'^root/', include('root.urls.en'), name='root'),
    url(r'^statement/', include('statement.urls.en'), name='statement'),
    url(r'^setting/', include('setting.urls.en'), name='setting'),
    url(r'^navigation/', include('navigation.urls.en'), name='navigation'),
    url(r'', include('main.urls.en'), name='main'),
]

