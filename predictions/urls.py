from django.urls import path
from . import views


urlpatterns = [
    path('', views.first_prediction, name="prediction" ),
]