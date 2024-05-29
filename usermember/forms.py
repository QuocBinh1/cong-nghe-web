# forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20 ,label= 'Tài khoản')
    password = forms.CharField(label='Mật Khẩu',widget=forms.PasswordInput )

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20 ,label= 'Tài khoản1')
    email = forms.EmailField(label='Gmail') 
    password1 = forms.CharField(label='Mật Khẩu1',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Nhập Lại Mật Khẩu',widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Mật khẩu không khớp.")
