from django import forms
from django.forms import fields
from .models import Lead, Empresa

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'nombres',
            'apellidos',
            'titulo',
            'email',
            'compania',
            'movil',
            'telefono',
            'descripcion',
            'agente'
        )

class EmpresaModelForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = (
            'nombre',
            'telefono',
            'website',
            'descripcion',
            'calleFacturacion',
            'ciudadFacturacion',
            'estadoFacturacion',
            'paisFacturacion',
            'codigoFacturacion'
        )

class LeadForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    
