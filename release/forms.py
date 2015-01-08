from django import forms
from contact.models import Contact
from .models import Release
from django.db.models import Q


class ReleaseDownloadForm(forms.Form):
    release = forms.ModelChoiceField(queryset=Release.objects.filter(podcast=False), required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data["email"]
        self.contact = Contact.objects \
            .filter(Q(email__iexact=email)).distinct()
        return self.cleaned_data["email"]

    def save(self, **kwargs):
        email = self.cleaned_data["email"]
        if not self.contact.exists():
            contact = Contact(email=email)
            contact.save()
