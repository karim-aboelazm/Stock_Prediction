from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,UserFollowedStocks
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',
                  'password1','password2')
class UserForm(forms.ModelForm):
    class Meta:
       model = User
       fields = ['username','first_name','last_name','email']


class ProfileForm(forms.ModelForm):
    class Meta:
       model = Profile
       fields = ['city','state','zip','phone_number','image']
       
       
       
class FollowedStockForm(forms.ModelForm):
    class Meta:
       model = UserFollowedStocks
       fields = ["user_followed_stocks"]