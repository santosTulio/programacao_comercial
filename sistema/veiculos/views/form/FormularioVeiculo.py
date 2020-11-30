from django import forms

from ...models import Veiculo


class FormularioVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'ano_fabricacao', 'modelo_fabricacao', 'marca', 'combustivel','valor']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': u'form-control'}),
            'marca': forms.TextInput(attrs={'class': u'form-control'}),
            'ano_fabricacao': forms.NumberInput(attrs={'class': u'form-control'}),
            'modelo_fabricacao': forms.NumberInput(attrs={'class': u'form-control'}),
            'combustivel': forms.Select(attrs={'class': u'form-control'}),
            'valor': forms.NumberInput(attrs={'class': u'form-control'}),
        }