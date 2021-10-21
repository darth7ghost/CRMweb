from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganizacionYLoginRequiredMixin(AccessMixin):
    #Verifica si el usuario actual está autenticado y es organizador
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.es_organizador:
            return redirect('lead_list')
        return super().dispatch(request, *args, **kwargs)