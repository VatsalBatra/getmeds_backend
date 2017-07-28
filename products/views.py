from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import meds,cart,cart_item
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from account.models import MyUser


def show_all(request):
	content = {'list_view':meds.objects.all()}

	return render(request,'products/show_meds.html',content)

@login_required
def inc_quantity(request,id = None):
	print(id)
	if request.method == 'GET':

		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')
		print("popopopopopopopopoasdagdjkhasgdmasbd")
		if  cart_item.objects.filter(title = title,orderer = request.user).exists() :
			print("sdagdjkhasgdmasbd")
			item = cart_item.objects.get(title = title,orderer = request.user)
			print(item);
			setattr(item,'quantity',quantity)
			item.save()

			#how to controle max  limit condition and display of error message from views.py
			#WRITE ELSE FOR THIS IF
		return HttpResponse("ok")

@login_required
def dec_quantity(request,id = None):
	if request.method == 'GET':

		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')
		print("popopopopopopopopoasdagdjkhasgdmasbd")
		if  cart_item.objects.filter(title = title,orderer = request.user).exists() :
			print("sdagdjkhasgdmasbd")
			item = cart_item.objects.get(title = title,orderer=request.user)
			print(item);
			setattr(item,'quantity',quantity)
			item.save()
			#how to controle max  limit condition and display of error message from views.py
		#WRITE ELSE FOR THIS IF
		return HttpResponse("ok")


@login_required
def remove_from_cart(request,id = None):
	if request.method == 'GET':
		title = request.GET.get('name','');
	
		item =cart_item.objects.get(title = title,orderer = request.user)

		item_id = item.id
		cart_item.objects.filter(id=item_id).delete();
		# context = {'message' : "item removed successfully",
		# 			'list_view':cart.objects.all()}
		# HOW TO DO USING REDIRECT AND REVERSE -EVEN WITHIUT MESSAGE HOW TO DO USING REVERSE AND REDIRECT
		# also render is not working WHY??
		# return render(request,'products/show_cart.html',context)
		return HttpResponse("ok")
	
	
@login_required
def show_cart(request,id = None):
	user = request.user;
	if request.method == 'GET':
		if user.is_authenticated():
			user = get_object_or_404(MyUser,pk = request.user.id)
			print(user)
			my_user_cart = get_object_or_404(cart,user = user)
			my_cart_items = my_user_cart.cart_item.all();
			# for my_cart_item in my_cart_items:
			# 	lis

			content = {'list_view':my_user_cart.cart_item.all()}
			return render(request,'products/show_cart.html',content)
			# HttpResponse("ok")
		else:
			content = {	'message':"please login to continue",
						'user':request.user}
			return render(request,'products/show_cart.html',content)


# MAKE IT FOR BOTH CAPUTAL AND SMALL
def search(request):
	if request.is_ajax() and request.GET:

		variable = request.GET.get('searched','').lower()
	
		meds_result = meds.objects.all();
		inventory = [];
		for med in meds_result:
			print(variable[0].lower() + "   " +med.title[0].lower() )
			if variable in med.title.lower() and variable[0].lower() == med.title[0].lower():
				inventory.append(med.title)


				
		context = {
			'output':inventory
		}
		return JsonResponse(context,safe = False)


@login_required
def add_to_cart(request,id = None):
	if request.method == 'GET':
		rate = request.GET.get('rate','');
		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')
		product = cart_item(title = title,orderer = request.user)
		print(request.user.id)
		if not cart.objects.filter(user = request.user).exists() :
			print("qwqwqwqwqwqqwq")
			# product = cart_item(title = title,quantity = quantity,rate = rate)
			setattr(product,'quantity',quantity)
			setattr(product,'rate',rate)
			product.save()
			shopping_cart = cart(user = request.user)
			shopping_cart.save()
			shopping_cart.cart_item.add(product.id)
			print(shopping_cart)

		else:
			#cart.objects.filter(user = request.user,cart_item= product.id).exists(): why not wotkingh ?????
			if cart_item.objects.filter(orderer = request.user,title= title).exists():
				print("dasdasdasdasdasdasd")
				shopping_cart= cart.objects.get(user = request.user);
				print(shopping_cart)

				item  = cart_item.objects.get(title = title,orderer  = request.user)
				original_quantity = getattr(item,'quantity');
				print(original_quantity);
				final_quantity =  original_quantity + int(quantity);
				setattr(item,'quantity',final_quantity);
				item.save();
				shopping_cart.save();	
				print(final_quantity);
			else:
				product = cart_item(title = title,quantity = quantity,rate = rate,orderer = request.user)
				print("zczxczczxczcz")
				
				product.save()
				shopping_cart= cart.objects.get(user = request.user);
				shopping_cart.cart_item.add(product.id)
		return HttpResponse("ok")




# METHID - CONSIDER CART AS ITEM WE STORE ITEM AND ON CART ALL SHOW TO ITEM ATTACHED TO CORESSPONding EMAIL 
	# k = get_object_or_404(MyUser,pk = request.user.id)
	# print(k.id);



	# if request.method == 'GET':
	# 	rate = request.GET.get('rate','');
	# 	title = request.GET.get('name','');
	# 	quantity = request.GET.get('quantity','')
	# 	product = cart_item.objects.get(title  = title)


	# 	print(request.user)
	# 	if not cart.objects.filter(title = title,user = k ).exists() :
	# 		print("opopopopopopop")
	# 		#can use similar way to get total rate of all the quantity
	# 		item = cart(title = title,quantity = quantity,user = k)

	# 		# setattr(item,'quantity',final_quantity)
	# 		b = getattr(item,'user')
	# 		print(b)
	# 		print("popopowqeqweqwmfnsdnlkasjdl;kaj")
	# 		# setattr(item,'user',request.user)
	# 		a = getattr(item,'user')
	# 		print(a)

	# 		item.save()

	# 	else:
	# 		print("12312312312312312312312312")
			

	# 		item = cart.objects.get(title = title,user = k);
	# 		original_quantity = getattr(item,'quantity')
	# 		print(original_quantity)
	# 		final_quantity =  original_quantity + int(quantity)
	# 		setattr(item,'quantity',final_quantity)
	# 		item.save();	
	# 		print(final_quantity)

	# 	return HttpResponse("ok")

	# 