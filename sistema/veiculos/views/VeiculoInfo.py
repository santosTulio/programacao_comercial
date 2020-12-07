from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from ..models import *
from sistema.utilitarios import AutenticacaoObrigatoria


class VeiculoInfo(AutenticacaoObrigatoria, DetailView):
    """
    View para Detalhar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculo'
    template_name = 'veiculos/info.html'
