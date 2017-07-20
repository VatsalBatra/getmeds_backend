from django.conf.urls import url

from .views import show_all,add_to_cart,remove_from_cart,cart_list,search


urlpatterns = [
   
	url(r'^all/$',show_all,name = "all"),
	url(r'^add/$',add_to_cart,name = "add_to_cart"),
	url(r'^remove/$',remove_from_cart,name = "remove_from_cart"),
	url(r'^cart/$',cart_list,name = "cart_list"),
	url(r'^all/search/$',search,name = "search")

    
    # url(r'^users/',include('social.apps.django_app.urls', namespace='social'))
    

]
