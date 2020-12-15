from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator

from veiculos.views.form import FormularioVeiculo
from django.views.generic import CreateView
from veiculos.models import Veiculo

from sistema.utilitarios import AutenticacaoObrigatoria

class VeiculoCreate(AutenticacaoObrigatoria,CreateView):
    """
    View para Criar veiculos cadastrados.
    """
    model = Veiculo
    template_name = 'veiculos/criar.html'
    form_class = FormularioVeiculo

    def post(self, request, *args, **kwargs):
        form = FormularioVeiculo(request.POST)
        if form.is_valid():
            veiculo = form.save()
            veiculo.save()
            return HttpResponseRedirect(reverse('veiculos:listar-veiculos'))
        return render(request, reverse('veiculos:criar-veiculo'), {'form': form})