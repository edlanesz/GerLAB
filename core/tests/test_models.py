from django.test import TestCase
from django.utils import timezone
from core.models import AtoNormativ, Autoridade

class AtoNormativTestCase(TestCase):
    def setUp(self):
        # Cria uma instância de Autoridade para usar no teste
        self.autoridade = Autoridade.objects.create(nome='Autoridade 1')

    def test_valores_incorretos(self):
        # Teste 1: Número duplicado
        self.assertFalse(self.testar_valores_incorretos(numero=1, ano=2023, ementa='Ementa 1', texto_normativo='Texto 1'))
        
        # Teste 2: Ano inválido
        self.assertFalse(self.testar_valores_incorretos(numero=2, ano=0, ementa='Ementa 2', texto_normativo='Texto 2'))

        # Teste 3: Assinante1 inválido
        self.assertFalse(self.testar_valores_incorretos(numero=3, ano=2023, ementa='Ementa 3', texto_normativo='Texto 3', assinante1_id=999))

    def test_valores_corretos(self):
        # Teste 4: Valores corretos
        self.assertTrue(self.testar_valores_corretos(numero=4, ano=2023, ementa='Ementa 4', texto_normativo='Texto 4', assinante1_id=self.autoridade.id))

        # Teste 5: Outros valores corretos
        self.assertTrue(self.testar_valores_corretos(numero=5, ano=2023, ementa='Ementa 5', texto_normativo='Texto 5', assinante1_id=self.autoridade.id))

    def testar_valores_incorretos(self, numero, ano, ementa, texto_normativo, assinante1_id=1):
        try:
            ato_normativ = AtoNormativ(
                numero=numero,
                ano=ano,
                doe_numero=1,
                doe_secao='Seção',
                doe_pagina='Página',
                dt_cadastro=timezone.now(),
                usr_cadastro='Usuário de cadastro',
                ementa=ementa,
                texto_normativo=texto_normativo,
                publicado='n',
                usr_alteracao='Usuário de alteração',
                usr_publicacao='Usuário de publicação',
                assinante1_id=assinante1_id,
                assinante2='Assinante 2',
                status='revisao',
                tipo_ato='portaria'
            )
            ato_normativ.full_clean()  # Verifica se ocorrem erros de validação
            return True
        except Exception as e:
            print(f"Erro durante o teste: {e}")
            return False

    def testar_valores_corretos(self, numero, ano, ementa, texto_normativo, assinante1_id=1):
        try:
            ato_normativ = AtoNormativ(
                numero=numero,
                ano=ano,
                doe_numero=1,
                doe_secao='Seção',
                doe_pagina='Página',
                dt_cadastro=timezone.now(),
                usr_cadastro='Usuário de cadastro',
                ementa=ementa,
                texto_normativo=texto_normativo,
                publicado='n',
                usr_alteracao='Usuário de alteração',
                usr_publicacao='Usuário de publicação',
                assinante1_id=assinante1_id,
                assinante2='Assinante 2',
                status='revisao',
                tipo_ato='portaria'
            )
            ato_normativ.full_clean()  # Verifica se ocorrem erros de validação
            return True
        except Exception as e:
            print(f"Erro durante o teste: {e}")
            return False
