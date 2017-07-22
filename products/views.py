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


def show_all(request):
	content = {'list_view':meds.objects.all()}

	return render(request,'products/show_meds.html',content)

def inc_quantity(request):
	if request.method == 'GET':
		rate = request.GET.get('rate','');
		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')
		print("popopopopopopopopoasdagdjkhasgdmasbd")
		if  cart.objects.filter(title = title,rate = rate).exists() :
			print("sdagdjkhasgdmasbd")
			item = cart.objects.get(title = title)
			print(item);
			setattr(item,'quantity',quantity)
			item.save()
			#how to controle max  limit condition and display of error message from views.py
			#WRITE ELSE FOR THIS IF
		return HttpResponse("ok")


def dec_quantity(request):
	if request.method == 'GET':
		rate = request.GET.get('rate','');
		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')
		print("popopopopopopopopoasdagdjkhasgdmasbd")
		if  cart.objects.filter(title = title,rate = rate).exists() :
			print("sdagdjkhasgdmasbd")
			item = cart.objects.get(title = title)
			print(item);
			setattr(item,'quantity',quantity)
			item.save()
			#how to controle max  limit condition and display of error message from views.py
		#WRITE ELSE FOR THIS IF
		return HttpResponse("ok")

def add_to_cart(request):
	if request.method == 'GET':
		rate = request.GET.get('rate','');
		title = request.GET.get('name','');
		quantity = request.GET.get('quantity','')
		item =cart(title = title,rate = rate)

		if  cart.objects.filter(title = title,rate = rate).exists() :
			print("opopopopopopop")
			item = cart.objects.get(title = title);
			#can use similar way to get total rate of all the quantity
			original_qantity = getattr(item,'quantity');
			final_quantity = original_qantity + int(quantity)
			setattr(item,'quantity',final_quantity)			
			item.save()

		else:
			original_qantity = getattr(item,'quantity');
			final_quantity = original_qantity + int(quantity)
			setattr(item,'quantity',final_quantity)	
			item.save()
		return HttpResponse("ok")


def remove_from_cart(request):
	if request.method == 'GET':
		rate = request.GET.get('rate','');
		title = request.GET.get('name','');
	
		item =cart.objects.get(title = title)
		item_id = item.id
		cart.objects.filter(id=item_id).delete();
		# context = {'message' : "item removed successfully",
		# 			'list_view':cart.objects.all()}
		# HOW TO DO USING REDIRECT AND REVERSE -EVEN WITHIUT MESSAGE HOW TO DO USING REVERSE AND REDIRECT
		# also render is not working WHY??
		# return render(request,'products/show_cart.html',context)
		return HttpResponse("ok")
	
	

def show_cart(request):
	content = {'list_view':cart.objects.all()}

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
	