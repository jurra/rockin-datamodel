from django import forms
from .models import Contact, Core

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CoreForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = "__all__"