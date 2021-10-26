from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Empresa, Lead, Producto, Tarea, Evento, Deal
from .forms import (
    LeadModelForm, EmpresaModelForm, CustomUserCreationForm, ProductoModelForm, TareaModelForm,
    EventoModelForm, DealModelForm
)

#CRUD - Create, Retrieve, Update, Delete + List
class indexView(TemplateView):
    template_name="mainapp/index.html"


class signUpView(CreateView):
    template_name="registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        print("usuario creado")
        return reverse("login")


# --- VIEWS PARA CONTACTOS ---
class leadListView(LoginRequiredMixin, ListView):
    template_name="leads/leads_list.html"
    context_object_name = "contactos"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Lead.objects.filter(
                organizacion=user.userprofile,
                agente__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                organizacion=user.agent.organizacion,
                agente__isnull=False
            )
            queryset = queryset.filter(agente__user=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(leadListView, self).get_context_data(**kwargs)
        queryset = Lead.objects.filter(
            organizacion=user.userprofile,
            agente__isnull=True
        )
        context.update({
            "leads_noasignados": queryset
        })
        return context

class leadDetailView(LoginRequiredMixin, DetailView):
    template_name="leads/lead_detail.html"
    context_object_name = "contacto"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Lead.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Lead.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

class leadCreatelView(LoginRequiredMixin, CreateView):
    template_name="leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("lead_list")

    # --- ENVIANDO EMAILS ---
    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organizacion = self.request.user.userprofile
        lead.save()
        send_mail(
            subject="¡Un nuevo contacto ha sido creado!",
            message="Ve al sitio CRMIPC2 para ver al nuevo contacto",
            from_email="test@crmipc2.com",
            recipient_list=["oscar.sierrach@gmail.com"]
        )
        return super(leadCreatelView, self).form_valid(form)

class leadUpdatelView(LoginRequiredMixin, UpdateView):
    template_name="leads/lead_update.html"
    form_class = LeadModelForm
    context_object_name = "contacto"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Lead.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Lead.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_success_url(self):
        return reverse("lead_list")
    
class leadDeletelView(LoginRequiredMixin, DeleteView):
    template_name="leads/lead_delete.html"
    context_object_name = "contacto"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Lead.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Lead.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_success_url(self):
        return reverse("lead_list")



# --- VIEWS PARA EMPRESAS ---
class empresaListView(LoginRequiredMixin, ListView):
    template_name="empresas/empresa_list.html"
    context_object_name = "empresas"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Empresa.objects.filter(
                organizacion=user.agent.organizacion,
                agente__isnull=False
            )
        else:
            queryset = Empresa.objects.filter(
                organizacion=user.agent.organizacion,
                agente__isnull=False
            )
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(empresaListView, self).get_context_data(**kwargs)
        queryset = Empresa.objects.filter(
            organizacion=user.userprofile,
            agente__isnull=True
        )
        context.update({
            "empresas_noasignadas": queryset
        })
        return context

class empresaDetailView(LoginRequiredMixin, DetailView):
    template_name="empresas/empresa_detail.html"
    context_object_name = "empresa"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Empresa.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Empresa.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

class empresaCreatelView(LoginRequiredMixin, CreateView):
    template_name="empresas/empresa_create.html"
    form_class = EmpresaModelForm

    def get_success_url(self):
        return reverse("empresa_list")

    def form_valid(self, form):
        empresa = form.save(commit=False)
        empresa.organizacion = self.request.user.userprofile
        empresa.save()
        return super(empresaCreatelView, self).form_valid(form)

class empresaUpdatelView(LoginRequiredMixin, UpdateView):
    template_name="empresas/empresa_update.html"
    form_class = EmpresaModelForm
    context_object_name = "empresa"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Empresa.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Empresa.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_success_url(self):
        return reverse("empresa_list")

class empresaDeletelView(LoginRequiredMixin, DeleteView):
    template_name="empresas/empresa_delete.html"
    context_object_name = "empresa"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Empresa.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Empresa.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_success_url(self):
        return reverse("empresa_list")



# --- VIEWS PARA PRODUCTOS ---
class productoListView(LoginRequiredMixin, ListView):
    template_name="productos/producto_list.html"
    context_object_name = "productos"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Producto.objects.filter(
                organizacion=user.agent.organizacion,
                agente__isnull=False
            )
        else:
            queryset = Producto.objects.filter(
                organizacion=user.agent.organizacion,
                agente__isnull=False
            )
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(productoListView, self).get_context_data(**kwargs)
        queryset = Producto.objects.filter(
            organizacion=user.userprofile,
            agente__isnull=True
        )
        context.update({
            "productos_noasignados": queryset
        })
        return context

class productoDetailView(LoginRequiredMixin, DetailView):
    template_name="productos/producto_detail.html"
    context_object_name = "producto"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Producto.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Producto.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

class productoCreatelView(LoginRequiredMixin, CreateView):
    template_name="productos/producto_create.html"
    form_class = ProductoModelForm

    def get_success_url(self):
        return reverse("producto_list")

    def form_valid(self, form):
        producto = form.save(commit=False)
        producto.organizacion = self.request.user.userprofile
        producto.save()
        return super(productoCreatelView, self).form_valid(form)

class productoUpdatelView(LoginRequiredMixin, UpdateView):
    template_name="productos/producto_update.html"
    form_class = ProductoModelForm
    context_object_name = "producto"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Producto.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Producto.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_success_url(self):
        return reverse("producto_list")

class productoDeletelView(LoginRequiredMixin, DeleteView):
    template_name="productos/producto_delete.html"
    context_object_name = "producto"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Producto.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Producto.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(agente__user=user)
        return queryset

    def get_success_url(self):
        return reverse("producto_list")



# --- VIEWS PARA TAREAS ---
class tareaListView(LoginRequiredMixin, ListView):
    template_name="tareas/tarea_list.html"
    context_object_name = "tareas"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Tarea.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Tarea.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

class tareaDetailView(LoginRequiredMixin, DetailView):
    template_name="tareas/tarea_detail.html"
    context_object_name = "tarea"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Tarea.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Tarea.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

class tareaCreatelView(LoginRequiredMixin, CreateView):
    template_name="tareas/tarea_create.html"
    form_class = TareaModelForm
    
    def get_success_url(self):
        return reverse("tarea_list")

    def form_valid(self, form):
        tarea = form.save(commit=False)
        tarea.organizacion = self.request.user.userprofile
        tarea.save()
        return super(tareaCreatelView, self).form_valid(form)

class tareaUpdatelView(LoginRequiredMixin, UpdateView):
    template_name="tareas/tarea_update.html"
    form_class = TareaModelForm
    context_object_name = "tarea"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Tarea.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Tarea.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

    def get_success_url(self):
        return reverse("tarea_list")

class tareaDeletelView(LoginRequiredMixin, DeleteView):
    template_name="tareas/tarea_delete.html"
    context_object_name = "tarea"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Tarea.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Tarea.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

    def get_success_url(self):
        return reverse("tarea_list")



# --- VIEWS PARA EVENTOS ---
class eventoListView(LoginRequiredMixin, ListView):
    template_name="eventos/evento_list.html"
    context_object_name = "eventos"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Evento.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Evento.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

class eventoDetailView(LoginRequiredMixin, DetailView):
    template_name="eventos/evento_detail.html"
    context_object_name = "evento"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Evento.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Evento.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

class eventoCreatelView(LoginRequiredMixin, CreateView):
    template_name="eventos/evento_create.html"
    form_class = EventoModelForm

    def get_success_url(self):
        return reverse("evento_list")

    def form_valid(self, form):
        evento = form.save(commit=False)
        evento.organizacion = self.request.user.userprofile
        evento.save()
        return super(eventoCreatelView, self).form_valid(form)

class eventoUpdatelView(LoginRequiredMixin, UpdateView):
    template_name="eventos/evento_update.html"
    form_class = EventoModelForm
    context_object_name = "evento"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Evento.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Evento.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

    def get_success_url(self):
        return reverse("evento_list")

class eventoDeletelView(LoginRequiredMixin, DeleteView):
    template_name="eventos/evento_delete.html"
    context_object_name = "evento"
    
    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Evento.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Evento.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

    def get_success_url(self):
        return reverse("evento_list")



# --- VIEWS PARA DEALS ---
class dealListView(LoginRequiredMixin, ListView):
    template_name="deals/deal_list.html"
    context_object_name = "deals"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Deal.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Deal.objects.filter(organizacion=user.agent.organizacion)
        return queryset

class dealDetailView(LoginRequiredMixin, DetailView):
    template_name="deals/deal_detail.html"
    context_object_name = "deal"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Deal.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Deal.objects.filter(organizacion=user.agent.organizacion)
            queryset = queryset.filter(relacionado__user=user)
        return queryset

class dealCreatelView(LoginRequiredMixin, CreateView):
    template_name="deals/deal_create.html"
    form_class = DealModelForm

    def get_success_url(self):
        return reverse("deal_list")

    def form_valid(self, form):
        deal = form.save(commit=False)
        deal.organizacion = self.request.user.userprofile
        deal.save()
        return super(dealCreatelView, self).form_valid(form)

class dealUpdatelView(LoginRequiredMixin, UpdateView):
    template_name="deals/deal_update.html"
    form_class = DealModelForm
    context_object_name = "deal"

    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Deal.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Deal.objects.filter(organizacion=user.agent.organizacion)
        return queryset

    def get_success_url(self):
        return reverse("deal_list")

class dealDeletelView(LoginRequiredMixin, DeleteView):
    template_name="deals/deal_delete.html"
    context_object_name = "deal"
    
    def get_queryset(self):
        user = self.request.user
        if user.es_organizador:
            queryset = Deal.objects.filter(organizacion=user.userprofile)
        else:
            queryset = Deal.objects.filter(organizacion=user.agent.organizacion)
        return queryset

    def get_success_url(self):
        return reverse("deal_list")





# --- VIEWS OBSOLETAS ---
# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

# --- CONTACTOS ---

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "contactos": leads
    }
    return render(request, "mainapp/leads_list.html", context)

def lead_detail(request, pk):
    contacto = Lead.objects.get(id=pk)
    context = {
        "contacto": contacto
    }
    return render(request, 'mainapp/lead_detail.html', context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        print('Recibiendo un post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print("El form es válido.")
            form.save()
            print("El contacto ha sido creado.")
            return redirect("/contactos")

    context = {
        "form": form
    }
    return render(request, 'mainapp/lead_create.html', context)

def lead_update(request, pk):
    contacto = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=contacto)
    if request.method == "POST":
        print('Recibiendo un post request')
        form = LeadModelForm(request.POST, instance=contacto)
        if form.is_valid():
            print("El form es válido.")
            form.save()
            print("El contacto ha sido actualizado.")
            return redirect("/contactos")
    context = {
        "form": form,
        "contacto": contacto
    }
    return render(request, 'mainapp/lead_update.html', context)

def lead_delete(request, pk):
    contacto = Lead.objects.get(id=pk)
    contacto.delete()
    return redirect("/contactos")


# --- EMRPESAS ---
def empresa_list(request):
    empresas = Empresa.objects.all()
    context = {
        "empresas": empresas
    }
    return render(request, "mainapp/empresa_list.html", context)

def empresa_detail(request, pk):
    empresas = Empresa.objects.get(id=pk)
    context = {
        "empresas": empresas
    }
    return render(request, 'mainapp/empresa_detail.html', context)

def empresa_create(request):

    form = EmpresaModelForm()
    if request.method == "POST":
        print('Recibiendo un post request')
        form = EmpresaModelForm(request.POST)
        if form.is_valid():
            print("El form es válido.")
            form.save()
            print("La empresa ha sido creada.")
            return redirect("/empresas")

    context = {
        "form": form
    }
    return render(request, 'mainapp/empresa_create.html', context)

def empresa_update(request, pk):
    empresas = Empresa.objects.get(id=pk)
    form = EmpresaModelForm(instance=empresas)
    if request.method == "POST":
        print('Recibiendo un post request')
        form = EmpresaModelForm(request.POST, instance=empresas)
        if form.is_valid():
            print("El form es válido.")
            form.save()
            print("La empresa ha sido actualizada.")
            return redirect("/empresas")
    context = {
        "form": form,
        "empresas": empresas
    }
    return render(request, 'mainapp/empresa_update.html', context)

def empresa_delete(request, pk):
    empresa = Empresa.objects.get(id=pk)
    empresa.delete()
    return redirect("/empresas")