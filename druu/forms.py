from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from . models import Profile


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Phone"}), required=False)
    address1= forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Address 1"}), required=False)
    address2= forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Address 2"}), required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"City"}), required=False)
    state = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"State"}), required=False)
    zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Zipcode"}), required=False)
    country = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Country"}), required=False)

    class Meta:
        model = Profile
        fields = ["phone", "address1", "address2", "city", "state", "zipcode", "country"]







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
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"Email"}), required=False)
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':"form-control", "placeholder":"First Name"}), required=False)
    last_name = forms.CharField(label="", max_length=100,  widget=forms.TextInput(attrs={'class':"form-control","placeholder":"last Name"}), required=False)
    gender = forms.CharField(label="", max_length=6,  widget=forms.TextInput(attrs={'class':"form-control","placeholder":"Gender"}), required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "gender")

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)





