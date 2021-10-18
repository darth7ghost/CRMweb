from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Lead(models.Model):
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    titulo = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    compania = models.CharField(max_length=45)
    movil = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    agente = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Empresa(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    website = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    calleFacturacion = models.CharField(max_length=45)
    ciudadFacturacion = models.CharField(max_length=45)
    estadoFacturacion = models.CharField(max_length=45)
    paisFacturacion = models.CharField(max_length=45)
    codigoFacturacion = models.CharField(max_length=45)

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.IntegerField(default=0)
    categoria = models.CharField(max_length=45)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)
    activo = models.BooleanField()

class Tarea(models.Model):
    nombre = models.CharField(max_length=45)
    fechaVencimiento = models.DateField()
    repetir = models.BooleanField()
    relacionado = models.ForeignKey("Agent", on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    prioridad = models.BooleanField()

class Evento(models.Model):
    titulo = models.CharField(max_length=45)
    de = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    para = models.ForeignKey("Lead", on_delete=models.CASCADE)
    repetir = models.BooleanField()
    ubicacion = models.CharField(max_length=45)
    relacionado = models.ForeignKey("Agent", on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)

    