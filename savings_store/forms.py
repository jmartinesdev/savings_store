from django import forms 

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