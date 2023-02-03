from django.urls import path
from .views import CategoriaApiView

urlpatterns = [
    # cuando se acceda a la ruta se llama a la funcionalidad
    path('categorias/', CategoriaApiView.as_view())
]