from django import forms
from .models import Projeto, RegimentoInterno, UnidadeAcademica, Discente, Matricula

class DiscenteForm(forms.Form):
    nome = forms.CharField(label='Nome do Discente', max_length=255)

class ParticipantesForm(forms.Form):
    discentes = forms.CharField(label='Discentes Participantes', required=False, widget=forms.Textarea(attrs={'rows': 4}))
    matriculas = forms.CharField(label='Matrículas dos Discentes', required=False, widget=forms.Textarea(attrs={'rows': 4}))

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['projeto', 'nome_projeto', 'docente_responsavel', 'modalidade', 'vigencia_inicio', 'vigencia_fim', 'fomento', 'laboratorio']
        error_messages = {
            'projeto': {
                'required': "Cadastro do Sisproj é obrigatório."
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['laboratorio'].widget = forms.HiddenInput()

class ExclusaoRegimentoInternoForm(forms.Form):
    regimento_id = forms.IntegerField(widget=forms.HiddenInput())

class ExclusaounidadeForm(forms.Form):
    unidade_id = forms.IntegerField(widget=forms.HiddenInput())
    


class RegimentoInternoForm(forms.ModelForm):
    class Meta:
        model = RegimentoInterno
        fields = ['pdf']

class UnidadeAcademicaForm(forms.ModelForm):
    class Meta:
        model = UnidadeAcademica
        fields = ['pdf']