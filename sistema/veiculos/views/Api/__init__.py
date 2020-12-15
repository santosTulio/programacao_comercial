from rest_framework import serializers
from rest_framework import generics

from veiculos.models import Veiculo

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        exclude = []

class VeiculosListAPI(generics.ListAPIView):
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()