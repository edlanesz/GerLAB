from django.db import models
from django.utils import timezone
import tempfile


class Apresentacao(models.Model):
    texto_ajustavel = models.TextField(null=False, verbose_name='Texto Para Tela Principal')

class Marca(models.Model):
    nome_marca=models.CharField(null=False,max_length=100, verbose_name='nome da marca do equipamento')

class Equipamento(models.Model):
    nome_equipamento= models.CharField(null=False,max_length=255, verbose_name='nome do equipamento')

class RegimentoInterno(models.Model):
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.CASCADE, related_name='regimentos_internos')
    pdf = models.FileField(upload_to='pdf_regimentos_internos/')
    nome_do_pdf = models.CharField(max_length=255, default="pedro")
    status = models.BooleanField(default=True)  
    
    def __str__(self):
        return f'Regimento Interno {self.id}'

class UnidadeAcademica(models.Model):
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.CASCADE, related_name='unidades_academicas_do_laboratorio')
    pdf = models.FileField(upload_to='pdf_unidades_academicas/', null=True, blank=True)

    def __str__(self):
        return f"Unidade Acadêmica para {self.laboratorio}"

    class Meta:
        db_table = 'unidade_academica'  # Nome correto da tabela no banco interno

class ImagemLaboratorio(models.Model):
    imagem = models.ImageField(upload_to='imagens_laboratorio/', null=True, verbose_name='Imagem do Laboratório')
    laboratorios = models.ManyToManyField('Laboratorio', blank=True, related_name='imagens_lab')
    data_upload = models.DateTimeField(default=timezone.now)  # Defina um valor padrão aqui
    def __str__(self):
        return f'Imagem {self.id}'

    def __str__(self):
        return f'Imagem {self.id}'
    
class GrupoDePesquisa(models.Model):
    nome_do_grupo = models.CharField(max_length=255,null=True, verbose_name='Nome do grupo de pesquisa')
    area = models.CharField(max_length=50, null=True, verbose_name='Área de atuação')
    link_grupo = models.URLField(verbose_name='Link do grupo de pesquisa', blank=True, null=True)

    def __str__(self):
        return self.nome_do_grupo
    


class Laboratorio(models.Model):

    nome_laboratorio = models.CharField(max_length=255, null=False, verbose_name="nome do laboratorio")
    responsavel = models.CharField(null=False,max_length=255,default="jose carlos", verbose_name='Usuário de cadastro')
    cpf_responsavel = models.CharField(max_length=14, null=True, blank=True)
    user_ldap_responsavel = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(verbose_name='email', null=False,default="meu_email@example.com")
    telefone = models.CharField(max_length=15,default="9299999",null=False,verbose_name='numero de telefone')
    unidade = models.CharField(null=True,max_length=255, verbose_name='unidade academica' , default="meu_email")
    rua = models.CharField(null=True, max_length=255,verbose_name='nome da rua do laboratorio' , default="meu_email@example.com")
    numero_rua = models.PositiveIntegerField(null=True,default="32232",verbose_name='numero da rua do laboratorio')
    cep = models.PositiveIntegerField(null=True,default="33323",verbose_name='cep do bairro do laboratorio')
    bairro= models.CharField(null=True, max_length=255,default="jose carlos", verbose_name='nome do bairro do laboratorio')
    andar = models.CharField(max_length=255, null=True, blank=True)
    sala = models.CharField(null=True, max_length=20, verbose_name='sala do laboratorio')
    funcionamento = models.CharField(null=True, max_length=255, verbose_name='nome do local de funcionamento do laboratorio')
    descricao = models.TextField(null=True, max_length=400, default="ou", verbose_name='descricao das atividades de pesquisa e ensino:')
    site = models.URLField(null=True, blank=True, verbose_name='Site do laboratório')
    link_pnipe = models.CharField(null=True,default="ou",max_length=255, verbose_name='link do pnipe')
    ato_anexo = models.BinaryField(null=True, verbose_name='Anexo do Ato', blank=True)
    unidades_academicas = models.ManyToManyField(UnidadeAcademica, related_name='laboratorios', blank=True)
    imagens = models.ManyToManyField(ImagemLaboratorio, related_name='laboratorios_lab', blank=True)
    grupos_de_pesquisa = models.ManyToManyField(GrupoDePesquisa, related_name='laboratorios', blank=True)
    aprovado = models.BooleanField(default=False, verbose_name='Aprovado')
    ocultar_laboratorio = models.BooleanField(default=False, verbose_name='Ocultar laboratório')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    
    def __str__(self):
        return self.nome_laboratorio

    def save(self, *args, **kwargs):
        # Obtém o estado atual do objeto do banco de dados (se existir)
        if self.pk:
            existing_lab = Laboratorio.objects.get(pk=self.pk)
            # Compara os campos relevantes para detectar alterações
            fields_to_check = [
                'nome_laboratorio', 'responsavel', 'cpf_responsavel', 'user_ldap_responsavel', 'email',
                'telefone', 'unidade', 'rua', 'numero_rua', 'cep', 'bairro', 'andar', 'sala', 
                'funcionamento', 'descricao', 'site', 'link_pnipe', 'ato_anexo', 'aprovado', 'ocultar_laboratorio'
            ]
            has_changes = any(
                getattr(existing_lab, field) != getattr(self, field)
                for field in fields_to_check
            )

            if not has_changes:
                # Se não houve mudanças, não atualiza o campo updated_at
                self.updated_at = existing_lab.updated_at

        super(Laboratorio, self).save(*args, **kwargs)

class Pos(models.Model):
    nome_do_Programa = models.CharField(max_length=255, null=True, verbose_name="nome pos")
    website = models.URLField(null=True, blank=True, verbose_name='link para o site')
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='pos')

    
class Formento(models.Model):

    nomedoparceito = models.CharField(max_length=255, null=True, verbose_name="nome do formento")
    selecao= models.CharField(max_length=255, null=True, verbose_name="selecao do formento")
    tipo =  models.CharField(max_length=30, null=True, verbose_name="fomento ou parceiria")
    
    edital=  models.CharField(max_length=255, null=True, verbose_name="nome do edital")
    numerodoformento= models.IntegerField(null=True,verbose_name="numero do edital")
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='Formentos')

class ResponsavelAssociado(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Responsável Associado")
    cpf = models.CharField(max_length=11, blank=True, null=True, verbose_name="CPF do Responsável Associado")
    user_ldap = models.CharField(max_length=255, blank=True, null=True, verbose_name="USER_LDAP do Responsável Associado")
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='responsaveis_associados')

    def __str__(self):
        return self.nome



class MembroLaboratorio(models.Model):

    nome_membro = models.CharField(max_length=80, null=True, verbose_name="nome do membro")
    funcao = models.CharField(max_length=100, null=True, verbose_name="função")
    curriculo_lattes = models.URLField(null=True, verbose_name="currículo Lattes")
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name="membros")

    def __str__(self):
        return self.nome_membro


class Infraestrutura(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, null=True, default=None)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, null=True, related_name='infraestrutura_equipamento', verbose_name='Nome do Equipamento lista')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, related_name='infraestrutura_marca', verbose_name='Nome da Marca lista')
    modelo = models.CharField(null=True, max_length=100, verbose_name='modelo do equipamento')
    finalidade = models.CharField(null=True, max_length=1000, verbose_name='finalidade do equipamento')
    status = models.BooleanField(default=True)  
    tombo =  models.CharField(null=True,default='-', max_length=300, verbose_name='tombo')
    quantidade = models.PositiveIntegerField(default=0)

class ImagemInfraestrutura(models.Model):
    imagem = models.ImageField(upload_to='infraestrutura_images/', null=True, blank=True, verbose_name='Imagem da Infraestrutura')
    infraestrutura = models.ForeignKey(Infraestrutura, on_delete=models.CASCADE, related_name='imagens_infraestrutura', verbose_name='Infraestrutura')

    def __str__(self):
        return f'Imagem da Infraestrutura #{self.id}'
    def __str__(self):
        return f"Infraestrutura #{self.id}"
    

    


class LaboratorioInfraestrutura(models.Model):
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='infraestruturas')
    infraestrutura = models.ForeignKey(Infraestrutura, on_delete=models.CASCADE)


class Projeto(models.Model):
    projeto = models.CharField(max_length=255)
    nome_projeto = models.CharField(max_length=255)
    docente_responsavel = models.CharField(max_length=255)
    modalidade = models.CharField(max_length=100)
    vigencia_inicio = models.DateField()
    vigencia_fim = models.DateField()
    fomento = models.CharField(max_length=100)
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.CASCADE, related_name='projetos_lab')

    def get_discentes_list(self):
        return list(self.discentes.values_list('nome', flat=True))

    def get_matriculas_list(self):
        return list(self.discentes.values_list('matricula__matricula', flat=True))  # Obtenha as matrículas

    def __str__(self):
        return self.projeto


class Discente(models.Model):
    nome = models.CharField(max_length=255)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='discentes', default=1)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    discente = models.ForeignKey(Discente, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=100)

    def __str__(self):
        return self.matricula




    
class Unidade(models.Model):
    unidade = models.CharField(max_length=100, verbose_name='Setor do usuário', default='Padrão')  # Adicione um valor padrão

    class Meta:
        db_table = 'unidade'  # Nome da tabela no banco de dados interno
