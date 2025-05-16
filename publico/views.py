from django.shortcuts import render
from core.models import Unidade, Laboratorio, Equipamento, RegimentoInterno, Unidade , Apresentacao
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Max
from core.models import Laboratorio,Projeto, Infraestrutura,LaboratorioInfraestrutura,ImagemLaboratorio, Marca, Equipamento, RegimentoInterno, UnidadeAcademica,ImagemInfraestrutura,GrupoDePesquisa,MembroLaboratorio, Pos, Formento, Apresentacao
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def paginar(list, limit_per_page, request): 
    paginator = Paginator(list, limit_per_page) 
    page = request.GET.get('page')
    atos = paginator.get_page(page)
    context = {
        'atos': atos,
        'total_pages': paginator.num_pages,
        'current_page': atos.number,
    }
    return context

@csrf_exempt
def geral(request):
    texto = request.POST.get('filtro')
    nome_laboratorio = request.POST.get('nome_laboratorio', '')
    nome_do_grupo = request.POST.get('grupo', '')
    responsavel = request.POST.get('responsavel', '')
    unidade = request.POST.get('unidade', '')
    pos = request.POST.get('pos', '')
    fomento = request.POST.get('fomento', '')
    projeto = request.POST.get('projeto', '')
    equipamento = request.POST.get('equipamento', '')
    aprovado = request.POST.get('aprovado', '')

    laboratorios = Laboratorio.objects.filter(ocultar_laboratorio=False)

    # Filtre os laboratórios com base no USER_LDAP do responsável e dos responsáveis associados
    if texto:
        laboratorios = laboratorios.filter(nome_laboratorio__icontains=texto)
    else:
        conditions = Q()
        if nome_laboratorio:
            conditions &= Q(nome_laboratorio__icontains=nome_laboratorio)
        if responsavel:
            conditions &= Q(responsavel__icontains=responsavel)
        if unidade:
            conditions &= Q(unidade__icontains=unidade)
        if pos:
            conditions &= Q(pos__nome_do_Programa__icontains=pos)
        if fomento:
            conditions &= Q(Formentos__numerodoformento__icontains=fomento)
        if nome_do_grupo:
            conditions &= Q(grupos_de_pesquisa__nome_do_grupo__icontains=nome_do_grupo)
        if equipamento:
            conditions &= Q(infraestrutura__equipamento__nome_equipamento__icontains=equipamento)
        if aprovado:
            conditions &= Q(aprovado=aprovado)
        laboratorios = laboratorios.filter(conditions)

    num = laboratorios.count()
    paginator = Paginator(laboratorios, 10)  # Define 10 laboratórios por página
    page = request.GET.get('page')
    laboratorios = paginator.get_page(page)

    # Ajuste aqui para contar apenas laboratórios não ocultos
    lab_count = Laboratorio.objects.filter(ocultar_laboratorio=False).count()
    infra_count = Equipamento.objects.count()
    apresentacao = Apresentacao.objects.first()
    
    options = Equipamento.objects.filter(nome_equipamento__icontains=equipamento)
    
    context = {
        'laboratorios': laboratorios,
        'lab_u': Laboratorio.objects.values('unidade').distinct(),
        'lab_count': lab_count,
        'infra_count': infra_count,
        'lab': Laboratorio.objects.all(),
        'texto_ajustavel': apresentacao.texto_ajustavel if apresentacao else "",
        'texto': apresentacao if apresentacao else "",
        'options': options,
        'num': num
    }

    return render(request, 'publico.html', context)

@csrf_exempt
def view(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id)

    regimentos_internos = RegimentoInterno.objects.filter(laboratorio=laboratorio)

    unidades_academicas = UnidadeAcademica.objects.filter(laboratorio=laboratorio)

    infraestruturas = Infraestrutura.objects.filter(laboratorio_id=laboratorio.id).filter(status=True)

    projetos = Projeto.objects.filter(laboratorio=laboratorio)

    membros = MembroLaboratorio.objects.filter(laboratorio=laboratorio)

    grupos_de_pesquisa = laboratorio.grupos_de_pesquisa.all()


    programas = Pos.objects.filter(laboratorio=laboratorio_id)

    formento = Formento.objects.filter(laboratorio=laboratorio_id)

    return render(request, 'view_publico.html', {'laboratorio': laboratorio, 'infraestruturas': infraestruturas, 'regimentos_internos': regimentos_internos, 'unidades_academicas': unidades_academicas, 'projetos': projetos, 'membros': membros, 'grupos_de_pesquisa': grupos_de_pesquisa, 'programas': programas, 'formento': formento})

