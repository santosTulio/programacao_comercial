from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.VeiculosList.as_view(),name='listar-veiculos'),
    path('criar/', views.VeiculoCreate.as_view(), name='criar-veiculo'),
    path('editar/<int:pk>', views.VeiculoUpdate.as_view(), name='editar-veiculo'),
    path('deletar/<int:pk>', views.VeiculoDelete.as_view(), name='deletar-veiculo'),
    path('<int:pk>', views.VeiculoInfo.as_view(), name='info-veiculo'),
    path('api/listar/', views.VeiculosListAPI.as_view(), name='api-listar-veiculo'),
]