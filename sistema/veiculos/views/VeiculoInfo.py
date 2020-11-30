from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from ..models import *

@method_decorator(login_required, name='dispatch')
class VeiculoInfo(DetailView):
    """
    View para Detalhar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculo'
    template_name = 'veiculos/info.html'
