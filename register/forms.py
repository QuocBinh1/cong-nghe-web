from django import forms

class register_Form(forms.Form):
    username = forms.CharField(max_length = 20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20 , widget=forms.PasswordInput) 

class login_Form(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length=20 , widget=forms.PasswordInput) 


