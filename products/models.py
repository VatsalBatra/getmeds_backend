from django.db import models
from account.models import MyUser



# Create your models here.
class meds(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 100, default = '')
	rate = models.CharField(max_length = 100, default = '')
	quantity  = models.IntegerField(default=0, blank=False);
	def __str__(self):
		return self.title
class cart(models.Model):


	title = models.CharField(max_length = 100, default = '')
	created_on = models.DateTimeField(auto_now_add = True)
	rate = models.CharField(max_length = 100, default = '')
	quantity  = models.IntegerField(default=0, blank=False);
	def __str__(self):
		return self.title
