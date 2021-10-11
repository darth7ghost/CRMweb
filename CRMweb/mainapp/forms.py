from django import forms
from .models import Lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'nombres',
            'apellidos',
            'agente'
        )

class LeadForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    
