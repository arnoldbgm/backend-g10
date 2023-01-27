from django.contrib import admin
from .models import ProductosModel
# Register your models here.

class ShowFields(admin.ModelAdmin):
    # Mostramos en formato tabla 
    list_display = ('nombre', 'precio', 'estado')


admin.site.register(ProductosModel, ShowFields)