from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    UserManager,
    PermissionsMixin,
    Group
    )
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    # class Meta:
    #     db_table = "User"


    id = models.AutoField(primary_key=True)
    unique_id = models.IntegerField()
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    
    is_superuser = models.BooleanField(default=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True) # validators should be a list
    bank_ac_number = models.CharField(max_length=80, null=True, blank=True)
    bank_ac_holder_name = models.CharField(max_length=115, null=True, blank=True)
    bank_ifsc_code = models.CharField(max_length=15, null=True, blank=True)
    is_bank_detail_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']



class EmployeeDetails(models.Model):
	employee_name =  models.CharField(max_length=50, blank=False, null=False)
	contact_no = models.PositiveIntegerField(blank=False, null=False)
  
class Wallet(models.Model):
	user = models.ForeignKey('User')
	available_bal = models.FloatField(default=0, null=True, blank=True)
	esi_bal = models.FloatField(default=0, null=True, blank=True)
	pension_bal = models.FloatField(default=0, null=True, blank=True)
	pf_bal = models.FloatField(default=0, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.available_bal = self.esi_bal + self.pension_bal + self.pf_bal

		super(Wallet,self).save(*args, **kwargs)

class TransactionStatus(object):
   SUCCESS = 1
   PENDING = 2
   CANCELLED = 3

class TransactionType(object):
   ESI = 1
   PENSION = 2
   PF = 3

class WalletTransaction(models.Model):
	TRANSACTIONTYPE_CHOICES = (
        (TransactionType.ESI, 'ESI'),
        (TransactionType.PENSION, 'PENSION'),
        (TransactionType.PF, 'PF')
        )
	TRANSACTIONSTATUS_CHOICES = (
        (TransactionStatus.SUCCESS, 'SUCCESS'),
        (TransactionStatus.PENDING, 'PENDING'),
        (TransactionStatus.CANCELLED, 'CANCELLED')
        )

	wallet = models.ForeignKey('Wallet')
	transaction_id = models.CharField(max_length=250)
	time = models.DateTimeField()
	transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTIONTYPE_CHOICES, default=TransactionType.ESI)
	transaction_status = models.PositiveSmallIntegerField(choices=TRANSACTIONSTATUS_CHOICES, default=TransactionStatus.PENDING)
	amount = models.FloatField(default=0)
	



