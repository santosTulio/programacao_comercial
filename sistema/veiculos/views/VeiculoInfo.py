from django.views.generic import DetailView
from veiculos.models import Veiculo

from sistema.utilitarios import AutenticacaoObrigatoria


class VeiculoInfo(AutenticacaoObrigatoria, DetailView):
    """
    View para Detalhar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculo'
    template_name = 'veiculos/info.html'
