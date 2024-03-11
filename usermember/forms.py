# forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20 ,label= 'Tài khoản')
    password = forms.CharField(label='Mật Khẩu',widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20 ,label= 'Tài khoản')
    password = forms.CharField(label='Mật Khẩu',widget=forms.PasswordInput)
    email = forms.EmailField() 
