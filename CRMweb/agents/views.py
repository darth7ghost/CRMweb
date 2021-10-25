import random
from django.db import reset_queries
from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from mainapp.models import Agent
from django.core.mail import send_mail
from .forms import AgentModelForm
from .mixins import OrganizacionYLoginRequiredMixin

# Create your views here.
class agentListView(OrganizacionYLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    def get_queryset(self):
        organizacion = self.request.user.userprofile
        return Agent.objects.filter(organizacion = organizacion)

class agentCreateView(OrganizacionYLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agent_list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.es_agente = True
        user.es_organizador = False
        contrasenia = random.randint(0, 10000000)
        user.set_password(f'{contrasenia}')
        user.save()
        Agent.objects.create(
            user = user,
            organizacion = self.request.user.userprofile
        )
        send_mail(
            subject = "Estás invitado a formar parte de GTxCRM.",
            message = f"Fuiste registrado como un agente. Por favor, inicia sesión para comenzar a trabajar.\nPuedes iniciar sesión con éste correo, y tu contraseña es: {contrasenia} .",
            from_email = "gtxcrm@gmail.com",
            recipient_list = [user.email]
        )
        return super(agentCreateView, self).form_valid(form)

class agentDetailView(OrganizacionYLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    def get_queryset(self):
        organizacion = self.request.user.userprofile
        return Agent.objects.filter(organizacion = organizacion)

class agentUpdateView(OrganizacionYLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    context_object_name = "agent"
    form_class = AgentModelForm
    def get_queryset(self):
        organizacion = self.request.user.userprofile
        return Agent.objects.filter(organizacion = organizacion)

    def get_success_url(self):
        return reverse("agent_list")

class agentDeleteView(OrganizacionYLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"
    def get_queryset(self):
        organizacion = self.request.user.userprofile
        return Agent.objects.filter(organizacion = organizacion)

    def get_success_url(self):
        return reverse("agent_list")