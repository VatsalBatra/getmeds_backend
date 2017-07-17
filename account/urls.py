from django.conf.urls import url
from .views import login, home, logout,add
urlpatterns = [
    url(r'^login/$', login, name ="login" ),
    url(r'^logout/$', logout, name ="logout" ),
    url(r'^(?P<id>\d+)/home/$', home, name = "home"),
    url(r'^add/$',add, name  = 'add'),
]