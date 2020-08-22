from django.shortcuts import render

from servicios.models import Servicio


# Create your views here.
def Services(request):

    services = Servicio.objects.all() # import all services already created
    return render(request, 'servicios/services.html', {'services':services})



def Show_on_table(request):

    tables = Servicio.objects.all()
    return render(request, 'servicios/tables.html', {'tables': tables})