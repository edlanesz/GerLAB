from django.shortcuts import render
from core.models import Laboratorio, Pos,  Infraestrutura
from django.db.models import Q
from django.http import QueryDict
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML

from django.shortcuts import render
from core.models import Laboratorio, Pos, Infraestrutura
from django.http import HttpResponseBadRequest
from django.template.loader import render_to_string
from weasyprint import HTML
from bs4 import BeautifulSoup
from weasyprint import HTML, pdf
from django.shortcuts import redirect
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse, HttpResponseRedirect 
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import HttpResponseRedirect


@csrf_exempt
def relatorio_na_tela(request):
    laboratorios = Laboratorio.objects.prefetch_related('unidades_academicas').all()
    todos_laboratorios = list(laboratorios)  # Criando uma cópia da lista de laboratórios
    responsaveis = Laboratorio.objects.values_list('responsavel', flat=True).distinct()
    unidades = Laboratorio.objects.values_list('unidade', flat=True).distinct()
    equipamentos = Infraestrutura.objects.values_list('equipamento__nome_equipamento', flat=True).distinct()
    context = {
        'laboratorios': laboratorios,
        'todos_laboratorios': todos_laboratorios,  # Passando a cópia da lista de laboratórios
        'responsaveis': responsaveis,
        'unidades': unidades,
        'equipamentos': equipamentos
    }
    return render(request, 'relatorio_na_tela.html', context)

@csrf_exempt
def filtrar_para_pdf(request):
    if request.method == 'POST':
        # Receber dados do modal de filtro
        responsavel_selecionado = request.POST.get('inputResponsavelPDF')
        unidade_selecionada = request.POST.get('inputUnidadePDF')
        laboratorio_selecionado = request.POST.get('inputLaboratorioPDF')
        equipamento_selecionado = request.POST.get('inputEquipamentoPDF')

        # Construir a URL para a visualização gerar_pdf com os filtros aplicados
        url = reverse('gerar_pdf')
        params = {}
        if responsavel_selecionado:
            params['responsavel'] = responsavel_selecionado
        if unidade_selecionada:
            params['unidade'] = unidade_selecionada
        if laboratorio_selecionado:
            params['laboratorio'] = laboratorio_selecionado
        if equipamento_selecionado:  # Adicione o equipamento selecionado aos parâmetros
            params['equipamento'] = equipamento_selecionado

        if params:
            url += '?' + '&'.join([f'{k}={v}' for k, v in params.items()])

        # Redirecionar para a visualização de PDF com os filtros aplicados
        return HttpResponseRedirect(url)
    else:
        return JsonResponse({'error': 'Método não permitido para esta visualização'})

@csrf_exempt
def gerar_pdf(request):
    if request.method == 'GET':
        responsavel_selecionado = request.GET.get('responsavel')
        unidade_selecionada = request.GET.get('unidade')
        laboratorio_selecionado = request.GET.get('laboratorio')
        equipamento_selecionado = request.GET.get('equipamento')

        # Inicializar a consulta com todos os laboratórios
        laboratorios_filtrados = Laboratorio.objects.all()

        # Aplicar os filtros usando a classe Q para permitir filtragem independente
        filtros = Q()
        if responsavel_selecionado:
            filtros |= Q(responsavel=responsavel_selecionado)
        if unidade_selecionada:
            filtros |= Q(unidade=unidade_selecionada)
        if laboratorio_selecionado:
            filtros |= Q(nome_laboratorio=laboratorio_selecionado)  # Corrigido para usar o campo 'nome_laboratorio'

        # Adicione o filtro por equipamento, se estiver presente
        if equipamento_selecionado:
            filtros |= Q(infraestrutura__equipamento__nome_equipamento__icontains=equipamento_selecionado)

        # Aplicar os filtros
        laboratorios_filtrados = laboratorios_filtrados.filter(filtros)

        html_string = render_to_string('html_gerar_relatorio.html', {'laboratorios': laboratorios_filtrados})

        html = HTML(string=html_string)
        pdf_bytes = html.write_pdf()

        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
        return response
    else:
        return HttpResponseBadRequest("Método não permitido para esta visualização")


    
def desenvolvimento(request):
    return render(request, 'desenvolvimento.html')

from django.shortcuts import redirect

# No seu views.py
@csrf_exempt
def filtrar_por_responsavel(request):
    if request.method == 'GET':
        responsavel_selecionado = request.GET.get('responsavel')
        unidade_selecionada = request.GET.get('unidade')
        laboratorio_selecionado = request.GET.get('laboratorio')
        equipamento_selecionado = request.GET.get('equipamento')

        # Recupera todos os laboratórios disponíveis
        todos_laboratorios = Laboratorio.objects.all()

        laboratorios_filtrados = todos_laboratorios

        if responsavel_selecionado and unidade_selecionada and laboratorio_selecionado and equipamento_selecionado:
            laboratorios_filtrados = laboratorios_filtrados.filter(
                Q(responsavel=responsavel_selecionado) |
                Q(unidade=unidade_selecionada) |
                Q(nome_laboratorio__icontains=laboratorio_selecionado) |
                Q(infraestrutura__equipamento__nome_equipamento__icontains=equipamento_selecionado)
            )
        elif responsavel_selecionado and unidade_selecionada and laboratorio_selecionado:
            laboratorios_filtrados = laboratorios_filtrados.filter(
                Q(responsavel=responsavel_selecionado) |
                Q(unidade=unidade_selecionada) |
                Q(nome_laboratorio__icontains=laboratorio_selecionado)
            )
        elif responsavel_selecionado and unidade_selecionada:
            laboratorios_filtrados = laboratorios_filtrados.filter(
                Q(responsavel=responsavel_selecionado) | Q(unidade=unidade_selecionada)
            )
        elif responsavel_selecionado:
            laboratorios_filtrados = laboratorios_filtrados.filter(responsavel=responsavel_selecionado)
        elif unidade_selecionada:
            laboratorios_filtrados = laboratorios_filtrados.filter(unidade=unidade_selecionada)
        elif laboratorio_selecionado:
            laboratorios_filtrados = laboratorios_filtrados.filter(nome_laboratorio__icontains=laboratorio_selecionado)
        elif equipamento_selecionado:
            laboratorios_filtrados = laboratorios_filtrados.filter(infraestrutura__equipamento__nome_equipamento__icontains=equipamento_selecionado)

        # Aplicando distinct() para evitar laboratórios duplicados
        laboratorios_filtrados = laboratorios_filtrados.distinct()

        # Recuperando todas as opções de filtro relevantes
        todos_responsaveis = Laboratorio.objects.values_list('responsavel', flat=True).distinct()
        todas_unidades = Laboratorio.objects.values_list('unidade', flat=True).distinct()
        todos_equipamentos = Infraestrutura.objects.values_list('equipamento__nome_equipamento', flat=True).distinct()

        # Renderize o HTML com os laboratórios filtrados
        

        # Retorne o HTML como uma resposta
        return render(request, 'relatorio_na_tela.html', {
            'laboratorios': laboratorios_filtrados,
            'todos_laboratorios': todos_laboratorios,  # Passando todos os laboratórios disponíveis
            'responsaveis': todos_responsaveis,
            'unidades': todas_unidades,
            'equipamentos': todos_equipamentos,
            'responsavel_selecionado': responsavel_selecionado,
            'unidade_selecionada': unidade_selecionada,
            'laboratorio_selecionado': laboratorio_selecionado,
            'equipamento_selecionado': equipamento_selecionado,
        })
    else:
        return HttpResponseBadRequest("Método não permitido para esta visualização")