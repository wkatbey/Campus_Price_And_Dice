from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column
from django.utils.translation import gettext_lazy as _
from users.models import User
from django.forms.widgets import SelectDateWidget
from django import forms


class UserCreationForm(forms.ModelForm):

    first_password = forms.CharField(label='Password', widget=forms.PasswordInput)
    conf_password = forms.CharField(label='Confirm Your Password', widget=forms.PasswordInput)
    
    is_maintainer_chkbox = forms.BooleanField(
        label='Do you own/manage a restaurant?', 
        widget=forms.CheckboxInput,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 
            'last_name', 'date_of_birth', 'first_password',
            'conf_password', 'is_maintainer')

        labels = {
            'is_maintainer': _('Do you own/manage a restaurant?'),
        }

        widgets = {
            'username': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs = {
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'date_of_birth': forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
            }),
        }

    def verify_password_entries(self):
        first_password = self.cleaned_data.get("first_password")
        conf_password = self.cleaned_data.get("conf_password")
        
        if first_password and conf_password and first_password != conf_password:
            raise forms.ValidationError("Woops! Your passwords don't match")
        
        return conf_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["first_password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 
            'date_of_birth', 'is_maintainer')
        labels = {
            'is_maintainer': _('Do you own/manage a restaurant?'),
        }
        widgets = {
            'is_maintainer': forms.CheckboxInput(attrs = {
                
            }),
            'username': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs = {
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'date_of_birth': forms.DateInput(attrs = {
                'class': 'form-control',
                'type': 'date'
            }),
        
        }


    def clean_password(self):
        return self.initial["password"]
    
    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

        return user

admin.site.register(User)

