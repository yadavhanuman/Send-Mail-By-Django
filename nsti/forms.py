from django import forms


class contactForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField( max_length=255)
    message=forms.CharField(widget=forms.Textarea,max_length=255)
    phone=forms.CharField(max_length=255)
   


