from django import forms

from sistema.veiculos.models import Veiculo


class VeiculoCreateForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'ano_fabricacao', 'modelo_fabricacao', 'marca', 'combustivel']

