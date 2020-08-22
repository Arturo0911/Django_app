from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Services, name ="services"),
    path('tables/', views.Show_on_table, name = "tables"),
]
