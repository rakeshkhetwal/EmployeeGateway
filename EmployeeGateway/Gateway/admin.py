from django.contrib import admin

# Register your models here.

from Gateway.models import *
from Gateway.forms import *
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        
        ('ID', {'fields': ('unique_id', )}),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'unique_id']

class WalletAdmin(admin.ModelAdmin):
    model = Wallet
    list_display = ['id', 'available_bal', 'esi_bal', 'pf_bal', 'pension_bal']

class WalletTransactionAdmin(admin.ModelAdmin):
    model = Wallet
    list_display = ['id', 'wallet', 'transaction_id', 'transaction_type', 'transaction_status', 'amount']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(WalletTransaction, WalletTransactionAdmin)