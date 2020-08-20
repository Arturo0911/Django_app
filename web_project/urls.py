from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name ="home"),
    path('shop/', views.Shop, name ="shop"),
    path('show/', views.show, name = "show"),
    path('blog/', views.Blog, name ="blog"),
    path('contact/', views.Contact, name ="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)