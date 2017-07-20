from django.shortcuts import render, get_object_or_404
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


def add_to_cart(request):
	return HttpResponse("ok")


def remove_from_cart(request):
	return HttpResponse("ok2")
	

def cart_list(request):
	return HttpResponse("ok3")


def search(request):

	variable = request.GET.get('searched','')
	
	meds_result = meds.objects.all();
	inventory = [];
	for med in meds_result:
		
		if variable in med.title and variable[0] is med.title[0]:
			inventory.append(med.title)

	for i in inventory:
				
	context = {
		'output':inventory
	}
	return JsonResponse(context,safe = False)
	