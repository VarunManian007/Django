from django.contrib.auth.models import User
from django import forms
class LoginForm(forms.form):
    email=forms.CharField(max_length=100)
    pss=forms.CharField(max_length=100)