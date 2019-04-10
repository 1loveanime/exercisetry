from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.
class PersonDetail(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	phone_regex = RegexValidator(regex=r'^\+639\d{9}$', message="Phone number must be entered in the format: '+639xxxxxxxx'")
	phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)