from django.shortcuts import render

from servicios.models import Servicio


# Create your views here.
def Services(request):

    services = Servicio.objects.all() # import all services already created
    return render(request, 'servicios/services.html', {'services':services})