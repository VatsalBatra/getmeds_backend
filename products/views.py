from django.shortcuts import render, get_object_or_404,redirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import meds,cart
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
		if  cart.objects.filter(title = title,user = request.user).exists() :
			print("sdagdjkhasgdmasbd")
			item = cart.objects.get(title = title,user = request.user)
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
		if  cart.objects.filter(title = title,user = request.user).exists() :
			print("sdagdjkhasgdmasbd")
			item = cart.objects.get(title = title,user =request.user)
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
	
		item =cart.objects.get(title = title,user = request.user)
		print(id)
		item_id = item.id
		cart.objects.filter(id=item_id).delete();
		# context = {'message' : "item removed successfully",
		# 			'list_view':cart.objects.all()}
		# HOW TO DO USING REDIRECT AND REVERSE -EVEN WITHIUT MESSAGE HOW TO DO USING REVERSE AND REDIRECT
		# also render is not working WHY??
		# return render(request,'products/show_cart.html',context)
		print(id)
		return HttpResponse("ok")
	
	
@login_required
def show_cart(request,id = None):
	user = request.user;
	if request.method == 'GET':
		if user.is_authenticated():
			user = get_object_or_404(MyUser,pk = request.user.id)
			mycart = cart.objects.filter(user = user)
			content = {'list_view':mycart}
			return render(request,'products/show_cart.html',content)
		else:
			content = {	'message':"please login to continue",
						'user':request.user}
			return render(request,'products/show_cart.html',content)



def search(request):
	if request.is_ajax() and request.GET:

		variable = request.GET.get('searched','')
	
		meds_result = meds.objects.all();
		inventory = [];
		for med in meds_result:
		
			if variable in med.title and variable[0] is med.title[0]:
				inventory.append(med.title)


				
		context = {
			'output':inventory
		}
		return JsonResponse(context,safe = False)


@login_required
def add_to_cart(request,id = None):
	k = get_object_or_404(MyUser,pk = request.user.id)
	print(k.id);


	if request.method == 'GET':
		rate = request.GET.get('rate','');
		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')



		print(request.user)
		if not cart.objects.filter(title = title,user = k ).exists() :
			print("opopopopopopop")
			#can use similar way to get total rate of all the quantity
			item = cart(title = title,quantity = quantity,user = k)
			
			med = meds.objects.get(title = title)

			# setattr(item,'quantity',final_quantity)
			b = getattr(item,'user')
			print(b)
			print("popopowqeqweqwmfnsdnlkasjdl;kaj")
			# setattr(item,'user',request.user)
			a = getattr(item,'user')
			print(a)

			item.save()

		else:
			print("12312312312312312312312312")
			

			item = cart.objects.get(title = title,user = k);
			original_quantity = getattr(item,'quantity')
			print(original_quantity)
			final_quantity =  original_quantity + int(quantity)
			setattr(item,'quantity',final_quantity)
			item.save();	
			print(final_quantity)

		return HttpResponse("ok")

	