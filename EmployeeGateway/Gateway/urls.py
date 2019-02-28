from django.conf.urls import url

from . import views

app_name='Gateway'

urlpatterns = [



url(r'^login/$', views.AdminLoginView.as_view(), name='login'),

url(r'^logout/$', views.AdminLogoutView.as_view(), name='logout'),

url(r'^create/', views.EmployeeIdentificationNoCreateView.as_view(), name="Employeecreate"),

url(r'^home/', views.EmployeeIdentificationNoListView.as_view(), name="employeelist"),

url(r'^home/details/(?P<pk>\d+)', views.EmployeeIdentificationNoDetailView.as_view(), name="y"),



url(r'^add-money-to-wallet/', views.AddMoneytoWallet.as_view(), name="add-money-to-wallet")







# url(r'^update/(?P<pk>\d+)', BusinessAdminUpdateView.as_view(), name="businessupdate"),
# url(r'^delete/(?P<pk>\d+)', BusinessAdminDeleteView.as_view(), name="businessdelete"),

    


]
