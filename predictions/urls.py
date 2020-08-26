from django.urls import path
from . import views


urlpatterns = [
    path('', views.first_prediction, name="prediction" ),
    path('api/', views._Get_data_from_json, name ="api"),
]