from django.db import models
from datetime import date

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    # A foto será salva numa pasta 'professores'
    foto = models.ImageField(upload_to='professores/', blank=True, null=True)
    descricao = models.TextField(help_text="Uma breve apresentação do professor")

    def __str__(self):
        return self.nome

class Plano(models.Model):
    PERIODOS = [
        ('/mês', '/mês'),
        ('/aula', '/aula'),
        ('/hora', '/hora'),
        ('/ano', '/ano'),
    ]

    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    periodo = models.CharField(
        max_length=20, 
        choices=PERIODOS, 
        default='/mês',
        verbose_name="Cobrança")
    beneficios = models.TextField(help_text="Separe os itens por quebra de linha")

    def get_beneficios_list(self):
        return self.beneficios.split('\n')

    def __str__(self):
        return self.titulo
    
class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Tel. do Responsável")
    ano_nascimento = models.IntegerField(help_text="Ex: 2015")
    # Podemos adicionar um campo de observação opcional
    observacoes = models.TextField(blank=True, null=True, help_text="Posição, alergias, etc.")

    def __str__(self):
        return f"{self.nome} ({self.ano_nascimento})"

    # Função Mágica: Calcula a idade automaticamente
    def idade(self):
        ano_atual = date.today().year
        return ano_atual - self.ano_nascimento

    # Função Mágica 2: Define a categoria automaticamente
    def categoria(self):
        id = self.idade()
        if id <= 6: return "Sub-6 (Baby)"
        elif id <= 10: return "Sub-10"
        elif id <= 13: return "Sub-13"
        elif id <= 15: return "Sub-15"
        elif id <= 17: return "Sub-17"
        else: return "Adulto"    

class Turma(models.Model):
    nome = models.CharField(max_length=50, help_text="Ex: Sub-11 Manhã")
    horario = models.CharField(max_length=50, help_text="Ex: 08:00 às 10:00")
    dias = models.CharField(max_length=50, help_text="Ex: Terças e Quintas")
    
    def __str__(self):
        return f"{self.nome} - {self.dias}"
