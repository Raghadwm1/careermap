from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Student

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

class CreateStudentUserForm(UserCreationForm):
    major = forms.CharField(required=True)
    level = forms.CharField(required=True)

    class Meta:
        # model = Student
        model = User
        fields = ['username', 'first_name', 'last_name', 'major', 'level', 'email', 'password1', 'password2']

class CreateExpertUserForm(UserCreationForm):
    major = forms.CharField(required=True)
    jobTitle = forms.CharField(required=True)

    class Meta:
        # model = Student
        model = User
        fields = ['username', 'first_name', 'last_name', 'major', 'jobTitle', 'email', 'password1', 'password2']
# from django import forms
# from .models import CustomUser

# class ProfilePictureForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['profile_picture']