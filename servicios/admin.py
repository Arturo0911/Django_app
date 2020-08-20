from django.contrib import admin
from .models import Servicio
# Register your models here.

class service_admin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Servicio, service_admin)