from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
    fullname = forms.CharField(
        error_messages={"Required":'This field is Required'},
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Full Name"
                }
            )
    )
    email = forms.EmailField(
        error_messages={"Invalid":'Enter e-mail address'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "E-mail"
                }
            )
    )
    Message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Your Message"
                }
            )
    )

class LoginForm(forms.Form):
    username = forms.CharField(),
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username),
        if qs.exists():
            raise forms.ValidationError('This user already exist. Tap another name.')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email),
        if qs.exists():
            raise forms.ValidationError('This e-mail already exist. Try another one.')
        return email
    
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password do not match')
        return data