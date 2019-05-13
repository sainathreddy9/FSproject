from django import forms

class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(max_length=120)
    price = forms.CharField()

class SignupForm(forms.Form):
    firstname = forms.CharField()
    username = forms.CharField(max_length=120)
    emailid = forms.CharField(max_length=120)
    phoneno = forms.CharField(max_length=120)
    password = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField()