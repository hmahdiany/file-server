import imp
from django import forms
from .models import Qcow

class QcowForm(forms.ModelForm):
    class Meta:
        model = Qcow
        fields = ('title', 'file')