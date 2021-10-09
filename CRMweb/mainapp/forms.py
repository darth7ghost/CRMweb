from django import forms

class LeadForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    
