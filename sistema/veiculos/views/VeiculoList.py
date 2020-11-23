from django.views.generic import ListView
from ..models import *

class VeiculosList(ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculos/listar.html'
