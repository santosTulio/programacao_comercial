from django.urls import path

from veiculos.views import VeiculoUpdate
from veiculos.views import VeiculosList
from veiculos.views import VeiculoInfo
from veiculos.views import VeiculoCreate
from veiculos.views import VeiculoDelete
from veiculos.views import VeiculosListAPI

urlpatterns = [
    path('', VeiculosList.as_view(),name='listar-veiculos'),
    path('criar/', VeiculoCreate.as_view(), name='criar-veiculo'),
    path('editar/<int:pk>', VeiculoUpdate.as_view(), name='editar-veiculo'),
    path('deletar/<int:pk>', VeiculoDelete.as_view(), name='deletar-veiculo'),
    path('<int:pk>', VeiculoInfo.as_view(), name='info-veiculo'),
    path('api/listar/', VeiculosListAPI.as_view(), name='api-listar-veiculo'),
]