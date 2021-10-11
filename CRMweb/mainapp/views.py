from django.shortcuts import render, HttpResponse, redirect
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')

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
            print("El contacto ha sido creado.")
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