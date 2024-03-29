from django import forms

'''
ContactForm()

Contains all of the fields attributes of the contact form in contact.html

https://docs.djangoproject.com/en/dev/topics/forms/

Args:
    forms.Form: Basic field to access form fields and widgets
'''

class ContactForm(forms.Form):
    name    = forms.CharField(widget=forms.TextInput(attrs={'text':'', 'name':'name', 'class': 'form-control', 'placeholder': 'Name'}))
    email   = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'Email'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'name':'subject', 'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'name':'message', 'class': 'form-control', 'placeholder': 'Message', 'rows': '14'}))
