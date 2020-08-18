from django.shortcuts import render, HttpResponse
# Create your views here.

def Home(request):

    return HttpResponse("<h1>Home page</h1>")

def Services(request):

    return HttpResponse("<h1>Service page</h1>")

def Shop(request):

    return HttpResponse("<h1>Shop page</h1>")

def Blog(request):

    return HttpResponse("<h1>blog page</h1>")

def Contact(request):

    return HttpResponse("<h1>Contact page</h1>")