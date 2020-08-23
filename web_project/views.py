from django.shortcuts import render, HttpResponse,redirect
from servicios.models import Servicio
# Create your views here.

def Home(request):

    return render(request, 'web_project/home.html')




def Shop(request):

    
    return render(request, 'web_project/shop.html')

def show(request):

    #message = "titulo: %r"%request.POST['title']

    if(request.POST['title'] and request.FILES['imagen'] and request.POST['description']):


        title = request.POST['title']
        imagen = request.FILES['imagen']
        content = request.POST['description']

        Data_saved = Servicio(titulo= title, contenido= content, imagen=imagen)
        Data_saved.save()
        messagge = "Datas was saved successfully"
        return redirect('/services/')
    else:
        message = "STOP!!! Data it's prohibided"
        return render(request, 'web_project/shop.html', {'message':message})







def Blog(request):

    return render(request, 'web_project/blog.html')

def Contact(request):

    return render(request, 'web_project/contact.html')