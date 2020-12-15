from django.views.generic import ListView
from veiculos.models import Veiculo

from sistema.utilitarios import AutenticacaoObrigatoria


class VeiculosList(AutenticacaoObrigatoria,ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculos/listar.html'
