from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import string









from django.shortcuts import render
from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView, ListView
# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers, exceptions, status, permissions, viewsets
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout   #, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from django.views.generic import FormView, RedirectView, TemplateView,ListView


from django.views.generic import FormView, RedirectView, TemplateView,ListView,DetailView,UpdateView


from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView, View, CreateView, DetailView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth.decorators import login_required, user_passes_test



from .models import *

from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User



# @csrf_exempt
# def payment(request):
#     print(request.method)
#     print(request.POST)
#     request_data = request.POST
#     amount = request_data["amount"]
#     user_unique_id = request_data["unique_id"]
#     transaction_type = request_data["transaction_type"]
#     time_of_payment = timezone.now()

#     # take this parameter in script
    



#     transaction_id = __id_generator__()
#     if transaction_type == "ESI":
#         transaction_type_id = TransactionType.ESI
#     if transaction_type == "PENSION":
#         transaction_type_id = TransactionType.PENSION
#     if transaction_type == "PF":
#         transaction_type_id = TransactionType.PF
#     print(int(user_unique_id))
    

#     y=UniqueIdentityDetails.objects.filter(unique_id=int(user_unique_id))
#     z=y.name
#     x=EmployeeDetails.objects.filter(employee_name = z)

#     salary = x.salary
#     print(y)
#     print(z)
#     print(x)


#     esi_bal = (salary*10)/100
#     pf_bal = (salary*5)/100
#     pension_bal = (salary*6)/100




#     user = UniqueIdentityDetails.objects.filter(unique_id=int(user_unique_id))
#     if user.exists():
#         user = user.first()
#         wallet, created = Wallet.objects.get_or_create(user=user)
#         try:
#             amount = int(amount)
#             WalletTransaction.objects.create(wallet=wallet, amount=int(amount),
#                                       transaction_type=transaction_type_id, time=time,
#                                        transaction_id=transaction_id, transaction_status=TransactionStatus.SUCCESS)
#             if transaction_type == "ESI":
#                 esi_bal = (salary*10)/100
#             if transaction_type == "PENSION":
#                 pf_bal = (salary*5)/100
#             if transaction_type == "PF":
#                 pension_bal = (salary*6)/100

#             wallet.save()
#             return HttpResponse("Success")
#         except:

#             WalletTransaction.objects.create(wallet=wallet, amount=amount,
#                                       transaction_type=transaction_type_id, time=time,
#                                        transaction_id=transaction_id, transaction_status=TransactionStatus.PENDING)
#             return HttpResponse("Fail")

#     else:
#         return HttpResponse("User Doesn't exist")
