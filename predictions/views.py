from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
import csv
from .modules_calc import covarianza, test, charts, fetch_data

# Create your views here.

def first_prediction(request):

    covariance_value = covarianza.covariance()
    beta_one = covarianza.population_intersection()
    beta_zero = covarianza.population_slop()

    #print(test._initialize())

    values_regretions = {
        'Covariance': covariance_value,
        'beta_one': beta_one,
        'beta_zero':beta_zero
    }

    """
        Using for each 
        values_regretions = [
        {'Covariance': covariance_value},
        {'beta_one': beta_one},
        {'beta_zero':beta_zero}
        ]
    """
    #charts.Generate_chart()
    return render(request, 'predictions/prediction.html', {'covarianza':values_regretions})

def _Get_data_from_json(request):
    data_object = {
        'abcisa':fetch_data._get_lists_x(),
        'ordenada': fetch_data._get_lists_y()
    }
    return JsonResponse(data_object)
    
    