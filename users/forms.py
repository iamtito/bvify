from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
        
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    job = forms.CharField(max_length=100, required=False, label='Profession')
    description = forms.CharField(widget=forms.Textarea,max_length=200, required=False, label='Describe yourself')

    class Meta:
        model = Profile
        fields = ['job','description','image']