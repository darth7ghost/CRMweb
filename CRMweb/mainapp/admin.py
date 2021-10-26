from re import A
from django.contrib import admin
from .models import User, Lead, Agent, userProfile, Empresa, Producto, Tarea, Evento, Estado, Deal

# Register your models here.
admin.site.register(User)
admin.site.register(userProfile)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(Empresa)
admin.site.register(Producto)
admin.site.register(Tarea)
admin.site.register(Evento)
admin.site.register(Estado)
admin.site.register(Deal)