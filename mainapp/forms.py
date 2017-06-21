from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)
