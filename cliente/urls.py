from django.urls import path, include
from . import views

urlpatterns = [
   
    path('listar_cliente/', views.listar_cliente, name='listar_cliente'),
    
   
]