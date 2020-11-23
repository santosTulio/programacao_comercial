from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.views.generic import UpdateView

from .form import VeiculoUpdateForm
from ..models import *



class VeiculoUpdate(UpdateView):
    """
    View para editar veiculos cadastrados.
    """
    model = Veiculo
    template_name = 'veiculos/editar.html'
    form_class = VeiculoUpdateForm

    def post(self, request, *args, **kwargs):
        form = VeiculoUpdateForm(request.POST)
        if form.is_valid():
            veiculo = form.save()
            veiculo.save()
            return HttpResponseRedirect(reverse('veiculos:listar-veiculos'))
        return render(request, reverse('veiculos:criar-veiculo'), {'form': form})