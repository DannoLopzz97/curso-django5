from django.urls import path
from .views import CategoriaLista, CategoriaDetalle

urlpatterns = [
    path('categorias', CategoriaLista.as_view(), name='categoria-lista'),
    path('categorias/<int:id>', CategoriaDetalle.as_view(), name='categoria-detalle'),
]