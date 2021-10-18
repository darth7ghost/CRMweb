from django import forms
from django.forms import fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, Empresa, Producto, Tarea, Evento

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

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
    
class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'codigo',
            'categoria',
            'precio',
            'descripcion',
            'activo'
        )

class TareaModelForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = (
            'nombre',
            'fechaVencimiento',
            'repetir',
            'relacionado',
            'descripcion',
            'prioridad'
        )

class EventoModelForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = (
            'titulo',
            'de',
            'para',
            'repetir',
            'ubicacion',
            'relacionado',
            'descripcion'
        )



# --- FORM OBSOLETO ---
class LeadForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    
