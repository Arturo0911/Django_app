from django.shortcuts import render, HttpResponse
from servicios.models import Servicio
# Create your views here.

def Home(request):

    return render(request, 'web_project/home.html')




def Shop(request):

    
    return render(request, 'web_project/shop.html')

def show(request):

    #message = "titulo: %r"%request.POST['title']
    title = request.POST['title']
    imagen = request.FILES['imagen']
    content = request.POST['description']

    Data_saved = Servicio(titulo= title, contenido= content, imagen=imagen)
    Data_saved.save()
    return render(request, 'servicios/services.html')

def Blog(request):

    return render(request, 'web_project/blog.html')

def Contact(request):

    return render(request, 'web_project/contact.html')