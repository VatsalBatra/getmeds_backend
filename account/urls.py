from django.conf.urls import url
from .views import login, home, logout,add,forgot_password,reset_password,change_password
urlpatterns = [
    url(r'^login/$', login, name ="login" ),
    url(r'^logout/$', logout, name ="logout" ),
    url(r'^(?P<id>\d+)/home/$', home, name = "home"),
    url(r'^add/$',add, name  = 'add'),
    url(r'^forgot_password/$',forgot_password,name = 'forgot_password'),
    url(r'^reset_password/$',reset_password,name = 'reset_password'),
    url(r'^reset/(?P<id>\d+)/(?P<otp>\d{4})/$', change_password, name='change-password'),
    # url(r'^success/$',set_password_success,name = set_success)
 	# url(r'',include('social_auth.urls'))
]