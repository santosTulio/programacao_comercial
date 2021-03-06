from django.contrib import admin
from ..models import Veiculo

class VeiculoAdmin(admin.ModelAdmin):
    """
    Admin para o model Veiculo
    """
    list_display = ['marca', 'modelo', 'ano_fabricacao', 'modelo_fabricacao', 'combustivel']
    search_fields = ['marca', 'modelo']
    list_filter = ['combustivel']
    exclude = []

admin.site.register(Veiculo, VeiculoAdmin)