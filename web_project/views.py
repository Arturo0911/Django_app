from django.shortcuts import render, HttpResponse
# Create your views here.

def Home(request):

    return render(request, 'web_project/home.html')
def Services(request):

    return render(request, 'web_project/services.html')

def Shop(request):

    return render(request, 'web_project/shop.html')

def Blog(request):

    return render(request, 'web_project/blog.html')

def Contact(request):

    return render(request, 'web_project/contact.html')