from django.db import models
from account.models import MyUser



# Create your models here.
class meds(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	title = models.CharField(max_length = 100, default = '')
	def __str__(self):
		return self.title

