from django.shortcuts import render
from datetime import datetime as dt
from django.http import HttpResponse
from django.template import loader
from app_service_watch.models import *
from app_service_watch.forms import *
 
# REALIZAR INDEX, CLIENTES, STAFF, SERVICIOS PRESTADOS, SERVICIOS EN CURSO.

def index(request):
    return render (request, "app_service_watch/index.html")

def clients(request):
    return render(request, "app_service_watch/clients.html")

def staff(request):
    return render(request, "app_service_watch/staff.html")

def staff_form(request):
    
    if request.method == 'POST':
        
        staffForm = StaffForm(request.POST)

        print(staffForm)

        if staffForm.is_valid():

            informacion = staffForm.cleaned_data    

            serv_prov_form = Staff(name=informacion['name'], completion_date=informacion['completion_date'],completed=informacion['completed'])

            serv_prov_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        staffForm = StaffForm()

    return render(request, "app_service_watch/staff_form.html", {"staffForm": staffForm})


def services_provided(request):
    
    serv_prov = ServicesProvided.objects.all()

    return render(request, "app_service_watch/services_provided.html", {"servicios_prestados" : serv_prov})

def services_provided_form(request):
    
    if request.method == 'POST':
        
        spForm = ServicesProvidedForm(request.POST)

        print(spForm)

        if spForm.is_valid():

            informacion = spForm.cleaned_data    

            serv_prov_form = ServicesProvided(name=informacion['name'], completion_date=informacion['completion_date'],completed=informacion['completed'])

            serv_prov_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        spForm = ServicesProvidedForm()

    return render(request, "app_service_watch/services_provided_form.html", {"spForm": spForm})


def pending_services(request):
    pend_serv = PendingServices.objects.all()
    return render(request, "app_service_watch/pending_services.html", {"servicios_pendientes" : pend_serv})

def pending_services_form(request):
    
    if request.method == 'POST':
        
        psForm = PendingServicesForm(request.POST)

        print(psForm)

        if psForm.is_valid():

            informacion = psForm.cleaned_data    

            pend_serv_form = PendingServicesForm(name=informacion['name'], status_update_date=informacion['status_update_date'],status=informacion['status'])

            pend_serv_form.save()

        return render(request, "app_service_watch/index.html")
    
    else:
        psForm = PendingServicesForm()

    return render(request, "app_service_watch/pending_services_form.html", {"psForm": psForm})

def search(request):
    if request.method == "POST":
        miFormulario = Search(request.POST)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            busquedaservicios = ServicesProvided.objects.filter(name__incontains=info["name"]) 
            return render(request, "app_service_watch/search.html", {"busquedaserv": busquedaservicios })
    else:
        miFormulario = Search()

    return render(request, "app_service_watch/search.html", {"formulario": miFormulario})
