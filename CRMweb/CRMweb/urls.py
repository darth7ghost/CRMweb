from django.contrib import admin
from django.urls import path
from mainapp.views import lead_detail, lead_list, lead_create
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('contactos/', views.lead_list, name="lead_list"),
    path('contactos/<int:pk>/', views.lead_detail, name="lead_detail"),
    path('contactos/crearcontacto/', views.lead_create, name='lead_create')
]
