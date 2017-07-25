from django.conf.urls import url

from .views import show_all,add_to_cart,remove_from_cart,search,show_cart,inc_quantity,dec_quantity


urlpatterns = [
   
	url(r'^all/$',show_all,name = "all"),
	url(r'^add/$',add_to_cart,name = "add_to_cart"),
	url(r'^cart/remove/$',remove_from_cart,name = "remove_from_cart"),
	url(r'^all/search/$',search,name = "search"),
	url(r'^all/cart/$',add_to_cart,name = "add_to_cart"),
	url(r'^(?P<id>\d+)/cart/$',show_cart,name = "cart"),
	url(r'^cart/increase/$',inc_quantity, name = "increase"),
	url(r'^cart/decrease/$',dec_quantity, name = "decrease"),

    
    # url(r'^users/',include('social.apps.django_app.urls', namespace='social'))
    

]
