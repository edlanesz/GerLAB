from django.urls import path, include
from . import views
from .views import edit
from .views import salvar_laboratorio
from .views import salvar_laboratorio
from .views import editar_infraestrutura
from .views import aprovados
from .views import pesquisar
from .views import editar_endereco
from .views import editar_laboratorio
from .views import visualizar_pdf
from .views import imagem_rgb
from .views import visualizar_membros_laboratorio

from .views import excluir_regimento_interno
from .views import editar_grupo_de_pesquisa
from . import views
from core import  views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from .views import buscar_nomes
from .views import excluir_responsavel_associado, editar_laboratorio

from .views import excluir_imagem_laboratorio
# from .views import gerar_pd
from .views import aprovar_laboratorio
from .views import cancelar_aprovacao
from .views import adicionar_formento
from .views import excluir_formento
from .views import editar_formento
from .views import adicionar_pos
from .views import excluir_pos
from .views import editar_pos
from .views import ocultar_laboratorio, cancelar_ocultacao, desocultar_laboratorio, criar_projeto
from django.views.static import serve




urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('equipamento/', views.equipamento, name='equipamento'),
    path('adicionar_equipamento/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('main/', views.main, name='main'),
    path('salvar_laboratorio/', views.salvar_laboratorio, name='salvar_laboratorio'),
    path('salvar_equipamento/', views.salvar_equipamento, name='salvar_equipamento'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('visualizar_arquivo/<int:laboratorio_id>/', views.visualizar_arquivo, name='visualizar_arquivo'),
    path('imagem_rgb/<int:imagem_id>/', views.imagem_rgb, name='imagem_rgb'),
    path('visualizar_laboratorio/<int:laboratorio_id>/', views.visualizar_laboratorio, name='visualizar_laboratorio'), # Adicione esta linha
    path('editar_endereco/<int:laboratorio_id>/', views.editar_endereco, name='editar_endereco'),
    path('editar_infraestrutura/<int:laboratorio_id>/', views.editar_infraestrutura, name='editar_infraestrutura'),
    path('editar_regimentos_internos/<int:laboratorio_id>/', views.editar_regimentos_internos, name='editar_regimentos_internos'),
    path('editar_unidades_academicas/<int:laboratorio_id>/', views.editar_unidades_academicas, name='editar_unidades_academicas'),
    path('visualizar_pdf/<int:unidade_academica_id>/', views.visualizar_pdf, name='visualizar_pdf'),
    path('visualizar_regimento_interno/<int:regimento_id>/', views.visualizar_regimento_interno, name='visualizar_regimento_interno'),
    path('editar_infraestrutura/<int:laboratorio_id>/', views.editar_infraestrutura, name='editar_infraestrutura'),
    path('adicionar_grupo_de_pesquisa/<int:laboratorio_id>/', views.adicionar_grupo_de_pesquisa, name='adicionar_grupo_de_pesquisa'),
    path('visualizar_membros_laboratorio/<int:laboratorio_id>/', views.visualizar_membros_laboratorio, name='visualizar_membros_laboratorio'),
    path('editar_laboratorio/<int:laboratorio_id>/<int:imagem_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('export-to-excel/', views.export_to_excel, name='export_to_excel'),
    path('delete_infra/<int:laboratorio_id>/', views.delete_infra, name='delete_infra'),
    path('change_status/<int:id>/', views.change_status, name='change_status'),
    path('change_status_pdf/<int:id>/', views.change_status_pdf, name='change_status_pdf'),
    path('excluir_imagem_laboratorio/<int:laboratorio_id>/<int:imagem_id>/', excluir_imagem_laboratorio, name='excluir_imagem_laboratorio'),
    path('excluir_regimento_interno/<int:regimento_id>/', excluir_regimento_interno, name='excluir_regimento_interno'),
    path('editar_grupo_de_pesquisa/<int:grupo_de_pesquisa_id>/', views.editar_grupo_de_pesquisa, name='editar_grupo_de_pesquisa'),
    path('excluir_grupo_de_pesquisa/<int:grupo_de_pesquisa_id>/', views.excluir_grupo_de_pesquisa, name='excluir_grupo_de_pesquisa'),
    path('editar-membro-laboratorio/<int:membro_id>/', views.editar_membro_laboratorio, name='editar_membro_laboratorio'),
    path('excluir-membro-laboratorio/<int:membro_id>/', views.excluir_membro_laboratorio, name='excluir_membro_laboratorio'),
    path('projetos/<int:laboratorio_id>/', views.projetos, name='projetos'),
    path('projetos/excluir/<int:projeto_id>/', views.excluir_projeto, name='excluir_projeto'),
    path('obter_nome_projeto/', views.obter_nome_projeto, name='obter_nome_projeto'),
    path('obter_detalhes_projeto/', views.obter_detalhes_projeto, name='obter_detalhes_projeto'),
    path('obter_vigencia_projeto/', views.obter_vigencia_projeto, name='obter_vigencia_projeto'),
    path('obter_modalidade_projeto/', views.obter_modalidade_projeto, name='obter_modalidade_projeto'),
    path('buscar_nomes/', buscar_nomes, name='buscar_nomes'),
    path('editar_laboratorio/<int:laboratorio_id>/<int:responsavel_id>/excluir/', excluir_responsavel_associado, name='excluir_responsavel_associado'),
    path('editar_laboratorio/<int:laboratorio_id>/<int:imagem_id>/', editar_laboratorio, name='editar_laboratorio'),
    path('excluir_responsavel_associado/<int:laboratorio_id>/<int:responsavel_id>/',
         views.excluir_responsavel_associado, name='excluir_responsavel_associado'),
    path('aprovar_laboratorio/<int:laboratorio_id>/', aprovar_laboratorio, name='aprovar_laboratorio'),
    path('cancelar_aprovacao/<int:laboratorio_id>/', cancelar_aprovacao, name='cancelar_aprovacao'),
   
    path('adicionar_formento/<int:laboratorio_id>/', views.adicionar_formento, name='adicionar_formento'),
    path('adicionar_pos/<int:laboratorio_id>/', views.adicionar_pos, name='adicionar_pos'),

    path('excluir_formento/<int:formento_id>/', excluir_formento, name='excluir_formento'),
    path('excluir_pos/<int:pos_id>/', excluir_pos, name='excluir_pos'),
    path('update_ocultar/<int:lab_id>/', views.update_oculto, name='update_oculto'),

    path('editar_formento/<int:laboratorio_id>/<int:formento_id>/', views.editar_formento, name='editar_formento'),
    path('editar_pos/<int:laboratorio_id>/<int:pos_id>/', views.editar_pos, name='editar_pos'),
    path('texto_ajustavel/', views.texto_ajustavel, name='texto_ajustavel'),
    path('processar_impressao/', views.processar_impressao, name='processar_impressao'),
    path('ocultar_laboratorio/<int:laboratorio_id>/', ocultar_laboratorio, name='ocultar_laboratorio'),
    path('cancelar_ocultacao/<int:laboratorio_id>/', cancelar_ocultacao, name='cancelar_ocultacao'),
    path('desocultar_laboratorio/<int:laboratorio_id>/', desocultar_laboratorio, name='desocultar_laboratorio'),
    path('excluir_regimento_interno/<int:regimento_id>/', views.excluir_regimento_interno,
         name='excluir_regimento_interno'),
    path('excluir_laboratorio/<int:laboratorio_id>/', views.excluir_laboratorio, name='excluir_laboratorio'),
    path('excluir_unidade/<int:unidade_id>', views.excluir_unidade, name='excluir_unidade'),
    path('editar_projeto/<int:projeto_id>/', views.editar_projeto, name='editar_projeto'),
    path('get_infra_data/', views.get_infra_data, name='get_infra_data'),
    path('salvar_edicao_infra/', views.salvar_edicao_infra, name='salvar_edicao_infra'),
    path('criar_projeto/', criar_projeto, name='criar_projeto'),
    path('restart/', views.restart_gunicorn, name='restart_gunicorn'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# Adicione esta linha para servir arquivos estáticos durante o desenvolvimento
