from django.contrib import admin
from django.urls import path
from mainapp.views import lead_detail, lead_list, lead_create, lead_update, lead_delete
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('contactos/', views.lead_list, name="lead_list"),
    path('contactos/<int:pk>/', views.lead_detail, name="lead_detail"),
    path('contactos/crearcontacto/', views.lead_create, name='lead_create'),
    path('contactos/<int:pk>/editarcontacto', views.lead_update, name="lead_update"),
    path('contactos/<int:pk>/eliminarcontacto', views.lead_delete, name="lead_delete")
]
