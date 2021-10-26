from django.db import models
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    es_organizador = models.BooleanField(default=True)
    es_agente = models.BooleanField(default=False)

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lead(models.Model):
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    titulo = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    movil = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    descripcion = models.TextField()
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    agente = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class Empresa(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    website = models.CharField(max_length=45)
    descripcion = models.TextField()
    calleFacturacion = models.CharField(max_length=45)
    ciudadFacturacion = models.CharField(max_length=45)
    estadoFacturacion = models.CharField(max_length=45)
    paisFacturacion = models.CharField(max_length=45)
    codigoFacturacion = models.CharField(max_length=45)
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    agente = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.nombre} - {self.telefono}'

class Producto(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.IntegerField(default=0)
    categoria = models.CharField(max_length=45)
    precio = models.FloatField()
    descripcion = models.TextField()
    activo = models.BooleanField()
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    agente = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.codigo} {self.nombre}'

class Tarea(models.Model):
    nombre = models.CharField(max_length=45)
    fechaVencimiento = models.DateField()
    repetir = models.BooleanField()
    relacionado = models.ForeignKey("Agent", on_delete=models.CASCADE)
    descripcion = models.TextField()
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    prioridad = models.BooleanField()

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=45)
    de = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    para = models.ForeignKey("Lead", on_delete=models.CASCADE)
    repetir = models.BooleanField()
    ubicacion = models.CharField(max_length=45)
    relacionado = models.ForeignKey("Agent", on_delete=models.CASCADE)
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Deal(models.Model):
    nombre = models.CharField(max_length=45)
    contacto = models.ForeignKey("Lead", on_delete=models.CASCADE)
    empresa = models.ForeignKey("Empresa", on_delete=models.CASCADE)
    estado = models.ForeignKey("Estado", null=True, blank=True, on_delete=models.SET_NULL)
    monto = models.FloatField()
    fechaCierre = models.DateField()
    descripcion = models.TextField()
    producto = models.ForeignKey("Producto", on_delete=models.CASCADE)
    organizacion = models.ForeignKey(userProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        userProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)