from django.urls import path
from . import views


urlpatterns = [
    path('', views.Services, name ="services"),
    path('tables/', views.Show_on_table, name = "tables"),
]
