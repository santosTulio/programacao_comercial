from django.urls import reverse_lazy
from django.views.generic import DeleteView
from veiculos.models import Veiculo

from sistema.utilitarios import AutenticacaoObrigatoria

class VeiculoDelete(AutenticacaoObrigatoria,DeleteView):
    """
    View para deletar veiculos cadastrados.
    """
    model = Veiculo
    template_name = 'veiculos/deletar.html'
    success_url = reverse_lazy('veiculos:listar-veiculos')