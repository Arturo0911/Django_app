from django.shortcuts import render, HttpResponse
from servicios.models import Servicio
# Create your views here.

def Home(request):

    return render(request, 'web_project/home.html')




def Shop(request):

    
    return render(request, 'web_project/shop.html')

def show(request):
    message = "titulo: %r"%request.GET['title']
    return HttpResponse(message)

def Blog(request):

    return render(request, 'web_project/blog.html')

def Contact(request):

    return render(request, 'web_project/contact.html')