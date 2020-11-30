from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView
from ..models import *

@method_decorator(login_required, name='dispatch')
class VeiculoDelete(DeleteView):
    """
    View para deletar veiculos cadastrados.
    """
    model = Veiculo
    template_name = 'veiculos/deletar.html'
    success_url = reverse_lazy('veiculos:listar-veiculos')