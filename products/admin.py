from django.contrib import admin

from .models import meds,cart,cart_item


# Register your models here.
@admin.register(meds)
class MedsAdmin(admin.ModelAdmin):
	list_display = ['title','rate']
	date_hierarchy = 'created_on'

@admin.register(cart)
class CartAdmin(admin.ModelAdmin):
	list_display = ['user']
	date_hierarchy = 'created_on'


@admin.register(cart_item)
class CartitemAdmin(admin.ModelAdmin):
	list_display = ['title','quantity','rate','orderer']


