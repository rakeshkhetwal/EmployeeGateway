from django import forms
from django.contrib.auth import forms as auth_forms
from Gateway.models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'unique_id')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'unique_id')