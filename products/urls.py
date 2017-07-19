from django.conf.urls import url

from .views import show_all


urlpatterns = [
   
    url(r'^all/',show_all,name = "all"),
    
    # url(r'^users/',include('social.apps.django_app.urls', namespace='social'))
    

]
