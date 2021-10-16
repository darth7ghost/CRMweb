from django.contrib import admin
from django.urls import path
from mainapp.views import lead_detail, lead_list, lead_create, lead_update, lead_delete, empresa_list, empresa_detail
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    # --- URLS PARA CONTACTOS ---
    path('contactos/', views.lead_list, name="lead_list"),
    path('contactos/<int:pk>/', views.lead_detail, name="lead_detail"),
    path('contactos/crearcontacto/', views.lead_create, name='lead_create'),
    path('contactos/<int:pk>/editarcontacto', views.lead_update, name="lead_update"),
    path('contactos/<int:pk>/eliminarcontacto', views.lead_delete, name="lead_delete"),
    # --- URLS PARA EMPRESAS ---
    path('empresas/', views.empresa_list, name = 'empresa_list'),
    path('empresas/<int:pk>/', views.empresa_detail, name="empresa_detail"),
    path('empresas/crearempresa/', views.empresa_create, name='empresa_create'),
    path('empresas/<int:pk>/editarempresa', views.empresa_update, name="empresa_update"),
    path('empresas/<int:pk>/eliminarempresa', views.empresa_delete, name="empresa_delete")
]
