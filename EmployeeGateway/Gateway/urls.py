from django.conf.urls import url

from . import views
from django.views.generic import TemplateView
app_name='Gateway'

urlpatterns = [



url(r'^login/$', views.AdminLoginView.as_view(), name='login'),

url(r'^logout/$', views.AdminLogoutView.as_view(), name='logout'),

url(r'^create/', views.EmployeeIdentificationNoCreateView.as_view(), name="Employeecreate"),

url(r'^home/', views.EmployeeIdentificationNoListView.as_view(), name="employeelist"),

url(r'^home/details/(?P<pk>\d+)', views.EmployeeIdentificationNoDetailView.as_view(), name="y"),
url(r'^g$', TemplateView.as_view(template_name="Employee/PAYMENT.html"), name='g'),



url(r'^add-money-to-wallet/', views.payment, name="add-money-to-wallet")







# url(r'^update/(?P<pk>\d+)', BusinessAdminUpdateView.as_view(), name="businessupdate"),
# url(r'^delete/(?P<pk>\d+)', BusinessAdminDeleteView.as_view(), name="businessdelete"),

    


]
