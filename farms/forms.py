from django import forms
from farms.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Juan Dela Cruz'}),
            'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'juandelacruz@gmail.com'}),
            'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the message'}),
            'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body of the message'}),
        }

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = "__all__"
        widgets = {
            'email_address':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'juandelacruz@gmail.com'}),
        }

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = WhatsNew
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'News Title'}),
            'description':forms.TextInput(attrs={'class':'form-control', 'placeholder':'News Description'}),
            'content':forms.TextInput(attrs={'class':'form-control', 'placeholder':'News Content'}),
            'category':forms.Select(attrs={'class':'form-control', 'placeholder':'Ex. General'}),
        }