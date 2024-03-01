from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Users

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Users
       # fields = ("username", "email","user_contact")
        fields = "__all__"
class CustomUserChangeForm(UserChangeForm):

    class Meta:




        model = Users
        fields = ("username", "email")

class RegistrationForm(forms.Form):
    
    email = forms.EmailField()
    password = forms.PasswordInput()
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    #user_contact= forms.CharField(max_length=100)

    #registration time

    
    #
    #id_no=forms.
    # rest of the fields

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
       # user_contact = cleaned_data.get("user_contact")
        

        # you can validate those here

    class Meta:
        model = Users
        fields = "__all__"