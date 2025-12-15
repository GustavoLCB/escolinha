from django.contrib import admin
from .models import Professor, Plano, Aluno

admin.site.register(Professor)
admin.site.register(Plano)

# Configuração especial para a lista de Alunos ficar bonita
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_nascimento', 'idade', 'categoria')
    search_fields = ('nome',) # Adiciona barra de pesquisa por nome
    list_filter = ('ano_nascimento',) # Adiciona filtro lateral por ano
