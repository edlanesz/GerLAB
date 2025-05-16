from django.contrib import admin
from .models import Laboratorio, Marca, Equipamento, Infraestrutura,LaboratorioInfraestrutura, RegimentoInterno

class Atodmin(admin.ModelAdmin):
    list_display = ('id', 'nome_laboratorio', 'bairro')
    list_filter = ('nome_laboratorio',)  # Correção aqui, usando uma tupla
    list_per_page = 10
    search_fields = ('nome_laboratorio',)  # Correção aqui, usando uma tupla

admin.site.register(Laboratorio)
admin.site.register(Infraestrutura)
admin.site.register(Marca)
admin.site.register(Equipamento)
admin.site.register(LaboratorioInfraestrutura)
admin.site.register(RegimentoInterno)