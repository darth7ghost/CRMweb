from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Empresa, Lead, Agent, Producto, Tarea, Evento
from .forms import (
    LeadModelForm, EmpresaModelForm, CustomUserCreationForm, ProductoModelForm, TareaModelForm,
    EventoModelForm
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
class leadListView(ListView):
    template_name="leads/leads_list.html"
    queryset = Lead.objects.all()
    context_object_name = "contactos"

class leadDetailView(DetailView):
    template_name="leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "contacto"

class leadCreatelView(CreateView):
    template_name="leads/lead_create.html"
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse("lead_list")
    # --- ENVIANDO EMAILS ---
    def form_valid(self, form):
        send_mail(
            subject="¡Un nuevo contacto ha sido creado!",
            message="Ve al sitio CRMIPC2 para ver al nuevo contacto",
            from_email="test@crmipc2.com",
            recipient_list=["oscar.sierrach@gmail.com"]
        )
        return super(leadCreatelView, self).form_valid(form)

class leadUpdatelView(UpdateView):
    template_name="leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name = "contacto"
    def get_success_url(self):
        return reverse("lead_list")
    
class leadDeletelView(DeleteView):
    template_name="leads/lead_delete.html"
    queryset = Lead.objects.all()
    context_object_name = "contacto"
    def get_success_url(self):
        return reverse("lead_list")



# --- VIEWS PARA EMPRESAS ---
class empresaListView(ListView):
    template_name="empresas/empresa_list.html"
    queryset = Empresa.objects.all()
    context_object_name = "empresas"


class empresaDetailView(DetailView):
    template_name="empresas/empresa_detail.html"
    queryset = Empresa.objects.all()
    context_object_name = "empresa"


class empresaCreatelView(CreateView):
    template_name="empresas/empresa_create.html"
    form_class = EmpresaModelForm
    def get_success_url(self):
        return reverse("empresa_list")

class empresaUpdatelView(UpdateView):
    template_name="empresas/empresa_update.html"
    queryset = Empresa.objects.all()
    form_class = EmpresaModelForm
    context_object_name = "empresa"
    def get_success_url(self):
        return reverse("empresa_list")

class empresaDeletelView(DeleteView):
    template_name="empresas/empresa_delete.html"
    queryset = Empresa.objects.all()
    context_object_name = "empresa"
    def get_success_url(self):
        return reverse("empresa_list")



# --- VIEWS PARA PRODUCTOS ---
class productoListView(ListView):
    template_name="productos/producto_list.html"
    queryset = Producto.objects.all()
    context_object_name = "productos"


class productoDetailView(DetailView):
    template_name="productos/producto_detail.html"
    queryset = Producto.objects.all()
    context_object_name = "producto"


class productoCreatelView(CreateView):
    template_name="productos/producto_create.html"
    form_class = ProductoModelForm
    def get_success_url(self):
        return reverse("producto_list")

class productoUpdatelView(UpdateView):
    template_name="productos/producto_update.html"
    queryset = Producto.objects.all()
    form_class = ProductoModelForm
    context_object_name = "producto"
    def get_success_url(self):
        return reverse("producto_list")

class productoDeletelView(DeleteView):
    template_name="productos/producto_delete.html"
    queryset = Producto.objects.all()
    context_object_name = "producto"
    def get_success_url(self):
        return reverse("producto_list")



# --- VIEWS PARA TAREAS ---
class tareaListView(ListView):
    template_name="tareas/tarea_list.html"
    queryset = Tarea.objects.all()
    context_object_name = "tareas"


class tareaDetailView(DetailView):
    template_name="tareas/tarea_detail.html"
    queryset = Tarea.objects.all()
    context_object_name = "tarea"


class tareaCreatelView(CreateView):
    template_name="tareas/tarea_create.html"
    form_class = TareaModelForm
    def get_success_url(self):
        return reverse("tarea_list")

class tareaUpdatelView(UpdateView):
    template_name="tareas/tarea_update.html"
    queryset = Tarea.objects.all()
    form_class = TareaModelForm
    context_object_name = "tarea"
    def get_success_url(self):
        return reverse("tarea_list")

class tareaDeletelView(DeleteView):
    template_name="tareas/tarea_delete.html"
    queryset = Tarea.objects.all()
    context_object_name = "tarea"
    def get_success_url(self):
        return reverse("tarea_list")



# --- VIEWS PARA EVENTOS ---
class eventoListView(ListView):
    template_name="eventos/evento_list.html"
    queryset = Evento.objects.all()
    context_object_name = "eventos"


class eventoDetailView(DetailView):
    template_name="eventos/evento_detail.html"
    queryset = Evento.objects.all()
    context_object_name = "evento"


class eventoCreatelView(CreateView):
    template_name="eventos/evento_create.html"
    form_class = EventoModelForm
    def get_success_url(self):
        return reverse("evento_list")

class eventoUpdatelView(UpdateView):
    template_name="eventos/evento_update.html"
    queryset = Evento.objects.all()
    form_class = EventoModelForm
    context_object_name = "evento"
    def get_success_url(self):
        return reverse("evento_list")

class eventoDeletelView(DeleteView):
    template_name="eventos/evento_delete.html"
    queryset = Evento.objects.all()
    context_object_name = "evento"
    def get_success_url(self):
        return reverse("evento_list")








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