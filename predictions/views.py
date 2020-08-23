from django.shortcuts import render, HttpResponse,redirect
import csv
from .modules_calc import covarianza

# Create your views here.

def first_prediction(request):

    covariance_value = covarianza.covariance()

    return render(request, 'predictions/prediction.html', {'covarianza':covariance_value})
    
    