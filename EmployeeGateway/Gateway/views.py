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



from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import string


def beforepayment(request):

    sk=UniqueIdentityDetails.objects.filter(unique_id)
    kk = sk.unique_id
    return render(request, 'Employee/PAYMENT.html', {'iden':kk})



@csrf_exempt
def payment(request):
    print(request.method)
    print(request.POST)
    request_data = request.POST
    # take this parameter in script
    if transaction_type == "ESI":
        transaction_type_id = TransactionType.ESI
    if transaction_type == "PENSION":
        transaction_type_id = TransactionType.PENSION
    if transaction_type == "PF":
        transaction_type_id = TransactionType.PF
    print(int(user_unique_id))
    

    y=UniqueIdentityDetails.objects.filter(unique_id=int(user_unique_id))
    z=y.name
    x=EmployeeDetails.objects.filter(employee_name = z)

    salary = x.salary
    print(y)
    print(z)
    print(x)


    # esi_bal = (salary*10)/100
    # pf_bal = (salary*5)/100
    # pension_bal = (salary*6)/100




    user = UniqueIdentityDetails.objects.filter(unique_id=int(user_unique_id))
    if user.exists():
        user = user.first()
        #wallet, created = Wallet.objects.get_or_create(user=user)
        try:
            amount = int(amount)
            WalletTransaction.objects.create(wallet=wallet, amount=int(amount),
                                      transaction_type=transaction_type_id, time=time,
                                       transaction_id=transaction_id, transaction_status=TransactionStatus.SUCCESS)
            if transaction_type == "ESI":
                esi_bal = (salary*10)/100
            if transaction_type == "PENSION":
                pf_bal = (salary*5)/100
            if transaction_type == "PF":
                pension_bal = (salary*6)/100

            wallet.save()
            return HttpResponse("Success")
        except:

            WalletTransaction.objects.create(wallet=wallet, amount=amount,
                                      transaction_type=transaction_type_id, time=time,
                                       transaction_id=transaction_id, transaction_status=TransactionStatus.PENDING)
            return HttpResponse("Fail")

    else:
        return HttpResponse("User Doesn't exist")





# goverment part
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('govthome')
    else:
        form = UserCreationForm()
    return render(request, 'govt/signup.html', {'form': form})



class GovtHome(TemplateView):
    template_name='Employee/home.html'
    



class GovtLoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/govt-home/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'govt/govt-login.html'
    permissionlogin_checker = None  
    model= User

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    #@method_decorator(user_passes_test(lambda u: BusinessDev.objects.get(user__username=username)))
    def dispatch(self, request, *args, **kwargs):
        print ("checkingcheking")
        return super(GovtLoginView, self).dispatch(request, *args, **kwargs)    

    
    def post(self, request, *args, **kwargs):
        print ("Posting started")

        print(request.user)
        usernamee = self.get_form_kwargs().get('data').get('username')
        passworde = self.get_form_kwargs().get('data').get('password')

        '''
            here passing the test, if the user is of businessdev team or not.
        '''
        

        if request.user.is_authenticated:
            print ("Login User Already")
            return HttpResponseRedirect('/govt-home/')

        elif User.objects.filter(username__iexact = usernamee).exists()==True:
            from django.contrib.auth import authenticate, login, logout
            from django.contrib.auth.decorators import user_passes_test

            print("passes user test")
            user = authenticate(username=usernamee, password=passworde)
            print (user)
            
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect('/govt-home/')
            else:
                return HttpResponseRedirect('/govt-login/')

        else:
            return HttpResponseRedirect('/govt-login/')



def UniversalIdentityNoCreateTemplate(request):
    return render(request, 'govt/govt-create.html')



# error aftyer some time


def UniversalIdentityNoCreateView(request):
    from random import randint
    x = randint(10000000, 99999999)

    def __id_generator__(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        from django.utils import timezone
        today_now = timezone.now()
        order_id = today_now.strftime("%Y%m%d%H%M%f")
        print(order_id)
        print("successfullly done")
        return order_id



    # xx=__id_generator__()
    name = request.POST.get('name')
    DOB= request.POST.get('DOB')
    unique_id= int(x)

    print(unique_id)
    print("success")
    gender=request.POST.get('gender')    
    residential_address = request.POST.get('residential_address') 
    rakesh = UniqueIdentityDetails(name=name, DOB=DOB, unique_id=unique_id, gender=gender,residential_address=residential_address)
    rakesh.save()
    return HttpResponseRedirect(reverse('Gateway:employeelist'))




# class GovtIdentityNoCreateView(CreateView):
#     model = UniqueIdentityDetails
#     fields=('user', 'name', 'DOB', 'gender', 'residential_address')
#     template_name="govt/govt-create.html"
#     success_url='/govt-home/'


#     @method_decorator(login_required(login_url='/govt-login/'))
#     def dispatch(self, request, *args, **kwargs):
#         print(request.user)
#         global usernamed
#         usernamed = request.user   
#         print("check") 
#         return super(EmployeeIdentificationNoCreateView, self).dispatch(request, *args, **kwargs)


#     def get(self, request, *args, **kwargs):
#         def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
#             from django.utils import timezone
#             today_now = timezone.now()
#             order_id = today_now.strftime("%Y%m%d%H%M%f")
#             print(order_id)
#             return order_id

#         r = UniqueIdentityDetails()

#         x= UniqueIdentityDetails.objects.all()
#         x.


#         return super(BaseCreateView, self).get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(EmployeeIdentificationNoCreateView, self).get_context_data(**kwargs)
    #     return context










# this is for managers            


class AdminLoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/home/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'Employee/Employee-Login.html'
    permissionlogin_checker = None  
    model= User

    def get_success_url(self):
        redirect_to = self.request.REQUEST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    #@method_decorator(user_passes_test(lambda u: BusinessDev.objects.get(user__username=username)))
    def dispatch(self, request, *args, **kwargs):
        print ("checkingcheking")
        return super(AdminLoginView, self).dispatch(request, *args, **kwargs)    

    
    def post(self, request, *args, **kwargs):
        print ("Posting started")

        print(request.user)
        usernamee = self.get_form_kwargs().get('data').get('username')
        passworde = self.get_form_kwargs().get('data').get('password')

        '''
            here passing the test, if the user is of businessdev team or not.
        '''
        if request.user.is_authenticated:
            print ("Login User Already")
            return HttpResponseRedirect('/home/')

        elif User.objects.filter(username__iexact = usernamee).exists()==True:
            from django.contrib.auth import authenticate, login, logout
            from django.contrib.auth.decorators import user_passes_test

            print("passes user test")
            user = authenticate(username=usernamee, password=passworde)
            print (user)
            
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect('/home/')
            else:
                return HttpResponseRedirect('/login/')

        else:
            return HttpResponseRedirect('/login/')


class AdminLogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/gateway/login/'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(AdminLogoutView, self).get(request, *args, **kwargs)



def search(request):

    template_name = 'search.html'

    query = request.GET.get('q', '')
    '''
    Additionally, .get allows you to provide an additional parameter of a default value which 
    is returned if the key is not in the dictionary. For example, 
    request.POST.get('sth', 'mydefaultvalue')
    '''
    if query:
        # query example
        results = MyEntity.objects.filter(name__icontains=query).distinct()
    else:
        results = []
    return render(
        request, template_name, {'results': results})



class EmployeeIdentificationNoCreateView(CreateView):
    model = EmployeeDetails
    fields=('employee_name', 'contact_no')
    template_name="Employee/EmployeeIdentification-create.html"
    success_url='/list/'
    @method_decorator(login_required(login_url='/gateway/login/'))
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        global usernamed
        usernamed = request.user   
        print("check") 
        return super(EmployeeIdentificationNoCreateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmployeeIdentificationNoCreateView, self).get_context_data(**kwargs)
        return context



    
class EmployeeIdentificationNoListView(ListView):
    
    template_name  = "Employee/EmployeeIdentification-list.html"
    model = UniqueIdentityDetails
    fields=('name', 'pk')
    @method_decorator(login_required(login_url='/gateway/login/'))
    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        global username
        username = request.user   
        print("check")
        return super(EmployeeIdentificationNoListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmployeeIdentificationNoListView, self).get_context_data(**kwargs)
        
        context['Attributes'] = UniqueIdentityDetails.objects.all()
        return context


class Paymented(DetailView):
    model = EmployeeDetails
    template_name  = "Employee/transactionledger.html"
    context_object_name='payment'


    
    def dispatch(self, request, *args, **kwargs):
        print(request.user) 
        cc=self.kwargs['pk']

        salary=10000

        global final
        final=EmployeeDetails.objects.filter(pk=cc).get()

        
        final.esi_bal=(final.salary*12)/100
        final.pension_bal=(final.salary*5)/100
        final.pf_bal = (final.salary*15)/100
      
        final.save()

        print(final.esi_bal)

        print("dbcjbjbjb   not successs")
        return super(Paymented, self).dispatch(request, *args, **kwargs)


    


    def get_context_data(self, **kwargs):
        context = super(Paymented, self).get_context_data(**kwargs)

        print(final.esi_bal)
        print("reacheddddd")
        context['detail'] = final

        return context


class EmployeeIdentificationNoDetailView(DetailView):
    model = EmployeeDetails
    template_name  = "Employee/EmployeeIdentification-detail.html"
    context_object_name='detail'





    # pk_url_kwarg = "pk"
    
    # @method_decorator(login_required(login_url='/gateway/login/'))
    # def dispatch(self, request, *args, **kwargs):
    #     print(request.user) 
        
    #     global y
    #     cc=self.kwargs['pk']

    #     # print(cc)
    #     # print("reached")
    #     # y=UniqueIdentityDetails.objects.filter(pk=cc)
    #     # print(y.gender)

    #     # xx=y['name']

    #     # print(xx)

    #     # print("yes sucess done")

        

    #     return super(EmployeeIdentificationNoDetailView, self).dispatch(request, *args, **kwargs)

    



# class BusinessAdminDeleteView(DeleteView):
#     fields=('created_by','admin_supporter_club_name', 'admin_name_of_supporter_club','contact_no_chairperson', 
#         'supporter_club_country','email_chairperson', 'facebook_link_admin','date_of_contact',
#          'converted_date', 'socialmedia_contacted','lead_status','first_reminder','second_reminder','third_reminder','remarks')
#     model = LeadAdmin
#     template_name="Business_Dev/Business-admin-delete.html"
#     success_url='/business-admin/home/'
#     @method_decorator(login_required(login_url='/business-admin/login/'))
#     def dispatch(self, request, *args, **kwargs):
#         print(request.user) 
#         print("hexy") 
#         return super(BusinessAdminDeleteView, self).dispatch(request, *args, **kwargs)


# class BusinessAdminUpdateView(UpdateView):
#     fields=('admin_supporter_club_name', 'admin_name_of_supporter_club','contact_no_chairperson', 
#         'supporter_club_country','email_chairperson', 'facebook_link_admin','date_of_contact',
#          'converted_date', 'socialmedia_contacted','lead_status','first_reminder','second_reminder','third_reminder','remarks')
#     model = LeadAdmin
#     template_name="Business_Dev/Business-admin-update.html"
#     success_url='/business-admin/home/'
#     @method_decorator(login_required(login_url='/business-admin/login/'))
#     def dispatch(self, request, *args, **kwargs):
#         print(request.user) 
#         print("hexy") 
#         return super(BusinessAdminUpdateView, self).dispatch(request, *args, **kwargs)



# class BusinessAdminCreateView(CreateView):
#     fields=('created_by','admin_supporter_club_name', 'admin_name_of_supporter_club','contact_no_chairperson', 
#         'supporter_club_country','email_chairperson', 'facebook_link_admin','date_of_contact',
#          'converted_date', 'socialmedia_contacted','lead_status','first_reminder','second_reminder','third_reminder','remarks')
#     model = LeadAdmin
#     template_name="Business_Dev/Business-admin-create.html"
#     success_url='/business-admin/home/'
#     @method_decorator(login_required(login_url='/business-admin/login/'))
#     def dispatch(self, request, *args, **kwargs):
#         print(request.user)
#         global usernamed
#         usernamed = request.user   
#         print("check") 
#         return super(BusinessAdminCreateView, self).dispatch(request, *args, **kwargs)

#     def get_initial(self):
#         return {'created_by': self.request.user}

#     def get_context_data(self, **kwargs):
#         context = super(BusinessAdminCreateView, self).get_context_data(**kwargs)
#         return context



    



# class BusinessAdminDetails(DetailView):
#     model = LeadAdmin
#     template_name  = "Business_Dev/Business-admin-details.html"
#     @method_decorator(login_required(login_url='/business-admin/login/'))
#     def dispatch(self, request, *args, **kwargs):
#         print(request.user) 
#         return super(BusinessAdminDetails, self).dispatch(request, *args, **kwargs)





# class AddMoneytoWallet(APIView):
    # def get(self, request, format=None):
    #     print(request.data)
    #     pass
# def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
# # return ''.join(random.choice(chars) for _ in range(size))
#     from django.utils import timezone
#     today_now = timezone.now()
#     order_id = today_now.strftime("%Y%m%d%H%M%f")
#     return order_id



        

            




