from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    company = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.name} / Apellido: {self.last_name} / Email: {self.email} / Compañía: {self.company}"    

class Staff(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return f"Nombre: {self.name} / Apellido: {self.last_name} / Email: {self.email}"

class ServicesProvided(models.Model):
    name = models.CharField(max_length=60)
    completion_date = models.DateField()
    completed = models.BooleanField()

    def __str__(self):
        return f"Servicio brindado: {self.name} / Completado el: {self.completion_date} / Entregado: {self.completed}"

class PendingServices(models.Model):
    name = models.CharField(max_length=60)
    status_update_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Servicio Pendiente: {self.name} / Actualizado: {self.status_update_date} / Estado: {self.status}"