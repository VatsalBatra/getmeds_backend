from django.db import models
from random import randint
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
	phone = models.CharField(max_length = 10 , null = True)

	
def create_otp(user = None, purpose = None):
    if not user:
        raise ValueError("Invalid Arguments");
    choices = []
    for choice_purpose, verbose in UserOTP.OTP_PURPOSE_CHOICES:
        choices.append(choice_purpose)
    if not purpose in choices:
        raise ValueError('Invalid Arguments');
    if UserOTP.objects.filter(user = user, purpose = purpose).exists():
        old_otp = UserOTP.objects.get(user = user, purpose = purpose)
        old_otp.delete();
    otp = randint(1000, 9999)
    otp_object = UserOTP.objects.create(user = user, purpose = purpose, otp = otp)
    return otp



def get_valid_otp_object(user = None, otp= None, purpose = None):
    if not user:
        raise ValueError("Invalid Arguments");
    choices = []
    for choice_purpose, verbose in UserOTP.OTP_PURPOSE_CHOICES:
        choices.append(choice_purpose)
    if not purpose in choices:
        raise ValueError('Invalid Arguments');
    try:
        otp_object = UserOTP.objects.get(user = user, purpose=purpose, otp=otp)
        return otp_object
    except UserOTP.DoesNotExist:
        return None










class UserOTP(models.Model):
	OTP_PURPOSE_CHOICES = (
		('FP','forgot password'),
		('AA','account activation')

		);
	user  = models.ForeignKey(MyUser)
	otp = models.CharField(max_length = 4)
	purpose = models.CharField(max_length =2,choices = OTP_PURPOSE_CHOICES)
	created_on = models.DateTimeField(auto_now_add = True)
	class Meta:
		unique_together = ['user','purpose']