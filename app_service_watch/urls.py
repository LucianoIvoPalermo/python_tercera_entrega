from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="Inicio"),
    path("clients/", clients, name="Clientes"),
    path("staff/", staff, name="Staff"),
    path("staff_form/", staff_form, name="StaffForm"),
    path("services_provided/", services_provided, name="Servicios Prestados"),
    path("services_provided_form/", services_provided_form, name="ServProvForm"),
    path("pending_services/", pending_services, name="Servicios Pendientes"),
    path("pending_services_form/", pending_services_form, name="PendServForm"),
    path("search/", search, name="Search Bar"),
]