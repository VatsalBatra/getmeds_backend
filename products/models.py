from django.db import models
from account.models import MyUser



# Create your models here.
class meds(models.Model):
	created_on = models.DateTimeField(auto_now_add = True,null = True)
	title = models.CharField(max_length = 100, default = '')
	rate = models.CharField(max_length = 100, default = '')
	# quantity  = models.IntegerField(default=0, blank=True)
	def __str__(self):
		return self.title

class cart_item(models.Model):
	title =  models.CharField(max_length = 100, default = '');
	quantity  = models.IntegerField(default=0, blank=False);
	rate = models.CharField(max_length = 100, default = '');
	created_on = models.DateTimeField(auto_now_add = True,null = True)
	orderer = models.ForeignKey(MyUser,related_name = 'orderer',default = '',null	=	True, on_delete=models.CASCADE)

class cart(models.Model):


	title = models.CharField(max_length = 100, default = '')
	created_on = models.DateTimeField(auto_now_add = True,null = True)
	# rate = models.CharField(max_length = 100, default = '')
	# quantity  = models.IntegerField(default=0, blank=False);
	user = models.ForeignKey(MyUser,related_name = 'user',default = '',null	=	True, on_delete=models.CASCADE)
	cart_item = models.ManyToManyField(cart_item,related_name = 'item',default = '')
	def get_model_fields(model):
		return model._meta.fields

	