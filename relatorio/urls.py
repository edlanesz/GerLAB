from django.urls import path
from .views import relatorio_na_tela, desenvolvimento, filtrar_por_responsavel, gerar_pdf, filtrar_para_pdf

urlpatterns = [
    path('relatorio-na-tela/', relatorio_na_tela, name='relatorio_na_tela'),
    path('desenvolvimento/', desenvolvimento, name='desenvolvimento'),
    path('filtrar-por-responsavel/', filtrar_por_responsavel, name='filtrar_por_responsavel'),
    path('gerar-pdf/', gerar_pdf, name='gerar_pdf'),
    path('filtrar_para_pdf/', filtrar_para_pdf, name='filtrar_para_pdf'),
]