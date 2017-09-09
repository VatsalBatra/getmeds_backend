from django.conf.urls import url

from .views import show_all,add_to_cart,remove_from_cart,search,show_cart,inc_quantity,dec_quantity,show_product,make_wishlist,make_payment_page,payment_total


urlpatterns = [
   
	url(r'^all/$',show_all,name = "all"),
	url(r'^(?P<id>\d+)/cart/remove/$',remove_from_cart,name = "remove_from_cart"),
	url(r'^all/search/$',search,name = "search"),
	url(r'^all/cart/$',add_to_cart,name = "add_to_cart"),
	url(r'^(?P<id>\d+)/cart/$',show_cart,name = "cart"),
	url(r'^(?P<id>\d+)/cart/increase/$',inc_quantity, name = "increase"),
	url(r'^(?P<id>\d+)/cart/decrease/$',dec_quantity, name = "decrease"),
	url(r'^all/item/$',show_product,name = "item_show"),
	url(r'^wishlist/$',make_wishlist,name = "wishlist"),
	url(r'^(?P<id>\d+)/cart/payment/$',make_payment_page,name = 'payment_page'),

    
    # url(r'^users/',include('social.apps.django_app.urls', namespace='social'))
    

]
