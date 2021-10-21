from django import forms
from django.forms import fields
from mainapp.models import Agent

class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
    