from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .form import VeiculoCreateForm
from django.views.generic import CreateView
from ..models import *


class VeiculoCreate(CreateView):
    """
    View para Criar veiculos cadastrados.
    """
    model = Veiculo
    template_name = 'veiculos/criar.html'
    form_class = VeiculoCreateForm

    def post(self, request, *args, **kwargs):
        form = VeiculoCreateForm(request.POST)
        if form.is_valid():
            veiculo = form.save()
            veiculo.save()
            return HttpResponseRedirect(reverse('veiculos:listar-veiculos'))
        return render(request, reverse('veiculos:criar-veiculo'), {'form': form})