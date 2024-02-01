from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from . models import Order


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
     
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        # Add Bootstrap class to new_password1 field
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].help_text = ''

        # Add Bootstrap class to new_password2 field
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password1'].help_text = ''



class UpdateUserForm(UserChangeForm):
    #hide password
    password = None

    #getting other fields
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"Email"}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"First Name"}) )
    last_name = forms.CharField(label="", max_length=100,  widget=forms.TextInput(attrs={'class':"form-control","placeholder":"last Name"}) )
    gender = forms.CharField(label="", max_length=6,  widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Gender"}) )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "gender")

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'customer', 'quantity', 'address', 'phone_number', 'date', 'status']


        


