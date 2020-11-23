from django.views.generic import DetailView
from ..models import *

class VeiculoInfo(DetailView):
    """
    View para Detalhar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculo'
    template_name = 'veiculos/info.html'
