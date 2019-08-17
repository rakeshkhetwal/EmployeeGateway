from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    UserManager,
    PermissionsMixin,
    Group
    )
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# class User(AbstractUser):
#     # class Meta:
#     #     db_table = "user"

#     unique_id = models.IntegerField()
#     first_name = models.CharField(max_length=255, null=True)
#     last_name = models.CharField(max_length=255, null=True)
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
    
#     is_superuser = models.BooleanField(default=True)
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=16, blank=True) # validators should be a list
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     objects = UserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

class CustomUser(AbstractUser):
    

    unique_id = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.email




# class ChequeSystem(models.Model):
#   bank_account = models.PositiveIntegerField(blank=False, null=False)
#   IFSC = models.CharField(max_length=100, blank=True, null=True)
#   bank = models.CharField(max_length=100, blank=True, null=True)
#   def __str__(self):
#     return self.bank


class UniqueIdentityDetails(models.Model):
  #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  name =  models.CharField(max_length=50, blank=True, null=True)
  DOB =  models.PositiveIntegerField(blank=True, null=True)
  unique_id = models.PositiveIntegerField(blank=True, null=True)
  gender = models.CharField(max_length=50, blank=True, null=True)
  residential_address = models.CharField(max_length=1000, blank=True, null=True)





class EmployeeDetails(models.Model):
  #uniqueidentitydetails = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  employee_name =  models.CharField(max_length=50, blank=True, null=True)
  contact_no = models.PositiveIntegerField(blank=True, null=True)
  bank_accounts = models.PositiveIntegerField(blank=True, null=True)
  IFSC = models.CharField(max_length=100, blank=True, null=True)
  bank = models.CharField(max_length=100, blank=True, null=True)
  salary = models.PositiveIntegerField(blank=True, null=True)
  
  esi_bal = models.FloatField(default=0, null=True, blank=True)
  pension_bal = models.FloatField(default=0, null=True, blank=True)
  pf_bal = models.FloatField(default=0, null=True, blank=True)
  #available_bal = models.FloatField(default=0, null=True, blank=True)
  def save(self, *args, **kwargs):

    self.esi_bal = (self.salary*15)/100
    self.pension_bal = (self.salary*10)/100
    self.pf_bal = (self.salary*5)/100

    super(EmployeeDetails,self).save(*args, **kwargs) 



  def __str__(self):
    return self.employee_name

  
# class Wallet(models.Model):
# 	user = models.ForeignKey('CustomUser')
# 	salary = models.FloatField(default=0, null=True, blank=True)
# 	esi_bal = models.FloatField(default=0, null=True, blank=True)
# 	pension_bal = models.FloatField(default=0, null=True, blank=True)
# 	pf_bal = models.FloatField(default=0, null=True, blank=True)
#   available_bal = models.FloatField(default=0, null=True, blank=True)
# 	def save(self, *args, **kwargs):

#     self.esi_bal = salary*
# 		self.available_bal = self.esi_bal + self.pension_bal + self.pf_bal
#     self.esi_bal = 

# 		super(Wallet,self).save(*args, **kwargs)

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
  wallet = models.ForeignKey('EmployeeDetails')
  transaction_id = models.CharField(max_length=250)
  transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTIONTYPE_CHOICES, default=TransactionType.ESI)
  transaction_status = models.PositiveSmallIntegerField(choices=TRANSACTIONSTATUS_CHOICES, default=TransactionStatus.PENDING)
  amount = models.FloatField(default=0)
  time_of_payment = models.DateTimeField(auto_now_add=True)
  #time_of_next_payment = models.DateTimeField(auto_now=True)
	



