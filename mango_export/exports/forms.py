from django import forms
from .models import MangoExport

class MangoExportForm(forms.ModelForm):
    class Meta:
        model = MangoExport
        fields = ['variety', 'description', 'price']
