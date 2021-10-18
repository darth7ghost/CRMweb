from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from mainapp.views import (
    indexView, leadListView, empresaListView, leadDetailView, empresaDetailView, leadCreatelView,
    empresaCreatelView, leadUpdatelView, empresaUpdatelView, leadDeletelView, empresaDeletelView,
    signUpView, productoCreatelView, productoDeletelView, productoDetailView, productoListView,
    productoUpdatelView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView.as_view(), name="index"),
    path('inicio/', indexView.as_view(), name="inicio"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', signUpView.as_view(), name="signup"),
    # --- URLS PARA CONTACTOS ---
    path('contactos/', leadListView.as_view(), name="lead_list"),
    path('contactos/<int:pk>/', leadDetailView.as_view(), name="lead_detail"),
    path('contactos/crearcontacto/', leadCreatelView.as_view(), name='lead_create'),
    path('contactos/<int:pk>/editarcontacto', leadUpdatelView.as_view(), name="lead_update"),
    path('contactos/<int:pk>/eliminarcontacto', leadDeletelView.as_view(), name="lead_delete"),
    # --- URLS PARA EMPRESAS ---
    path('empresas/', empresaListView.as_view(), name = 'empresa_list'),
    path('empresas/<int:pk>/', empresaDetailView.as_view(), name="empresa_detail"),
    path('empresas/crearempresa/', empresaCreatelView.as_view(), name='empresa_create'),
    path('empresas/<int:pk>/editarempresa', empresaUpdatelView.as_view(), name="empresa_update"),
    path('empresas/<int:pk>/eliminarempresa', empresaDeletelView.as_view(), name="empresa_delete"),
    # --- URLS PARA PRODUCTOS ---
    path('productos/', productoListView.as_view(), name = 'producto_list'),
    path('productos/<int:pk>/', productoDetailView.as_view(), name="producto_detail"),
    path('productos/crearproducto/', productoCreatelView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editarproducto', productoUpdatelView.as_view(), name="producto_update"),
    path('productos/<int:pk>/eliminarproducto', productoDeletelView.as_view(), name="producto_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)