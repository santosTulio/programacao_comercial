from django.db import models


class CombustivelChoices(models.IntegerChoices):
    ETANOL = 1, 'Etanol'
    FLEX = 2, 'Flex'
    GASOLINA = 3, 'Gasolina'

class Veiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    modelo_fabricacao = models.IntegerField()
    combustivel = models.SmallIntegerField(choices=CombustivelChoices.choices)

    def __str__(self):
        return f"{self.marca} - {self.modelo} ({self.ano_fabricacao}/{self.modelo_fabricacao})"
