from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from mainapp.models import Agent
from .forms import AgentModelForm

# Create your views here.
class agentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    def get_queryset(self):
        return Agent.objects.all()

class agentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    def get_success_url(self):
        return reverse("agent_list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organizacion = self.request.user.userprofile
        agent.save()
        return super(agentCreateView, self).form_valid(form)

class agentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    def get_queryset(self):
        return Agent.objects.all()

class agentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    context_object_name = "agent"
    form_class = AgentModelForm
    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agent_list")

class agentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"
    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agent_list")