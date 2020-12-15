from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import UpdateView

from veiculos.views.form.FormularioVeiculo import FormularioVeiculo
from veiculos.models import Veiculo

from sistema.utilitarios import AutenticacaoObrigatoria


class VeiculoUpdate(AutenticacaoObrigatoria,UpdateView):
    """
    View para editar veiculos cadastrados.
    """
    model = Veiculo
    template_name = 'veiculos/editar.html'
    form_class = FormularioVeiculo

    def post(self, request, *args, **kwargs):
        form = FormularioVeiculo(request.POST)
        if form.is_valid():
            veiculo = form.save()
            veiculo.save()
            return HttpResponseRedirect(reverse('veiculos:listar-veiculos'))
        return render(request, reverse('veiculos:editar-veiculo'), {'form': form})