from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name ="home"),
    path('services/', views.Services, name ="services"),
    path('shop/', views.Shop, name ="shop"),
    path('blog/', views.Blog, name ="blog"),
    path('contact/', views.Contact, name ="contact"),
]