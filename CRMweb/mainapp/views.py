from django.shortcuts import render, HttpResponse, redirect
from .models import Empresa, Lead, Agent
from .forms import LeadForm, LeadModelForm, EmpresaModelForm

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

# --- VIEWS PARA CONTACTOS ---
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


# --- VIEWS PARA EMPRESAS ---
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