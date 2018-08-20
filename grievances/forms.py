from django import forms
from . import models

class ComplainForm(forms.ModelForm):
    class Meta:
        model = models.Complain
        fields = ['title', 'body']

class RespondForm(forms.ModelForm):
    class Meta:
        model = models.Complain
        fields = ['status', 'comments']