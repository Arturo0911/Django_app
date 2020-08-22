from django.shortcuts import render, HttpResponse
import csv

# Create your views here.

def first_prediction(request):

    lista_values = []
    """
    f = open("predictions/predicition.txt")

    for i in f:
        lista_values.append(i)
    """
    
    with open('servicios/servicio.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista_values.append(row)
    
    return HttpResponse(lista_values)
    
    