from django.shortcuts import render, HttpResponse, redirect
from .models import Lead, Agent
from .forms import LeadForm

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

    form = LeadForm()
    if request.method == "POST":
        print('Recibiendo un post request')
        form = LeadForm(request.POST)
        if form.is_valid():
            print("El form es válido.")
            print(form.cleaned_data)
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            agente = Agent.objects.first()
            Lead.objects.create(
                nombres = nombres,
                apellidos = apellidos,
                agente = agente
            )
            print("El contacto ha sido creado.")
            return redirect("/contactos")

    context = {
        "form": form
    }
    return render(request, 'mainapp/lead_create.html', context)
