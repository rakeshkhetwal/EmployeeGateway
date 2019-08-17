from django.conf.urls import url

from . import views
from django.views.generic import TemplateView
app_name='Gateway'

urlpatterns = [


url(r'^home/$', TemplateView.as_view(template_name="Employee/home.html"), name='homy'),

#this is for goverment portal for accesss of managers


url(r'^govt-signup/$', views.signup, name='signup'),




url(r'^govt-login/$', views.GovtLoginView.as_view(), name='govtlogin'),
url(r'^govt-home/$', views.GovtHome.as_view(), name='govthome'),

url(r'^govt-template/', views.UniversalIdentityNoCreateTemplate, name="govtcreatetemplate"),

url(r'^govt-create/', views.UniversalIdentityNoCreateView, name="govtcreated"),




# this is for managers

# url(r'^home/', views.Home.as_view(), name="home"),

url(r'^login/$', views.AdminLoginView.as_view(), name='login'),

url(r'^logouts/$', views.AdminLogoutView.as_view(), name='logout'),




url(r'^create/', views.EmployeeIdentificationNoCreateView.as_view(), name="create"),



url(r'^list/', views.EmployeeIdentificationNoListView.as_view(), name="employeelist"),

url(r'^home/details/(?P<pk>\d+)', views.EmployeeIdentificationNoDetailView.as_view(), name="detail"),





#payment gateway
url(r'^g$', TemplateView.as_view(template_name="Employee/PAYMENT.html"), name='g'),



# url(r'^add-money-to-wallet/', views.payment, name="add-money-to-wallet")


url(r'^transactionledger/(?P<pk>\d+)', views.Paymented.as_view(), name="transaction")







# url(r'^update/(?P<pk>\d+)', BusinessAdminUpdateView.as_view(), name="businessupdate"),
# url(r'^delete/(?P<pk>\d+)', BusinessAdminDeleteView.as_view(), name="businessdelete"),

    


]
