from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from veiculos.models import Veiculo
from veiculos.views.form import FormularioVeiculo


class TestViewVeiculosList(TestCase):
    def setUp(self):
        self.url = reverse('listar-veiculos')
        Veiculo(marca='Chevrolet', modelo='aaa', ano_fabricacao=2001, modelo_fabricacao=2001, combustivel=3, valor=10000).save()
        Veiculo(marca='Fiat', modelo='Uno', ano_fabricacao=2000, modelo_fabricacao=2001, combustivel=2, valor=15000).save()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get('lista_veiculos')), 2)

class TestViewVeiculosNew(TestCase):

    def setUp(self):
        self.url = reverse('criar-veiculo')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)

    def test_post(self):
        data = {
            'marca': 'Chevrolet',
            'modelo': 'Celta',
            'ano_fabricacao': 2001,
            'modelo_fabricacao': 2001,
            'combustivel': 2,
            'valor': 1
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 'Chevrolet')

class TestViewVeiculosEdit(TestCase):

    def setUp(self):
        self.instance = Veiculo.objects.create(marca='Chevrolet', modelo='Celta', ano_fabricacao=2001, modelo_fabricacao=2001, combustivel=3)
        self.url = reverse('deletar-veiculo', kwargs={'pk': self.instance.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertIsInstance(response.context.get('form'), FormularioVeiculo)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)
        self.assertEqual(response.context.get('object').valor, 15000)

    def test_post(self):
        data = {
            'marca': 'Chevrolet',
            'modelo': 'Celta',
            'ano_fabricacao': 2001,
            'modelo_fabricacao': 2001,
            'combustivel': 2,
            'valor': 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().marca, 'Chevrolet')
        self.assertEqual(Veiculo.objects.first().pk, self.instance.pk)


class TestViewVeiculosDelete(TestCase):

    def setUp(self):
        self.instance = Veiculo.objects.create(marca='Chevrolet', modelo='Celta', ano_fabricacao=2001, modelo_fabricacao=2001, combustivel=3)
        self.url = reverse('deletar-veiculo', kwargs={'pk': self.instance.pk})

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context.get('object'), Veiculo)
        self.assertEqual(response.context.get('object').pk, self.instance.pk)

    def test_post(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar-veiculos'))
        self.assertEqual(Veiculo.objects.count(), 0)


class TestModelVeiculo(TestCase):
    def setUp(self):
        self.instance = Veiculo(marca='Chevrolet', modelo='Celta', ano_fabricacao=datetime.now().year, modelo_fabricacao=2001,
                                combustivel=3, valor=10000).save()

    def test_is_new(self):
        self.assertTrue(self.instance.veiculo_novo)
        self.instance.ano_fabricacao = datetime.now().year - 5
        self.assertFalse(self.instance.veiculo_novo)

    def test_years_use(self):
        self.assertEqual(self.instance.anos_de_uso, 0)
        self.instance.ano_fabricacao = datetime.now().year - 5
        self.assertEqual(self.instance.anos_de_uso, 5)