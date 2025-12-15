from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Importação de segurança
from .models import Professor, Plano, Aluno # Importamos os modelos

def index(request):
    return render(request, 'escolinha/index.html')

def professores(request):
    # Pega todos os professores do banco de dados
    lista_professores = Professor.objects.all()
    context = {'professores': lista_professores}
    return render(request, 'escolinha/professores.html', context)

def valores(request):
    # Pega todos os planos do banco de dados
    lista_planos = Plano.objects.all()
    context = {'planos': lista_planos}
    return render(request, 'escolinha/valores.html', context)

def metodologia(request):
    return render(request, 'escolinha/metodologia.html')

# Nova View Protegida
@login_required # Isso garante que SÓ quem fez login pode ver
def lista_alunos(request):
    # Pega todos os alunos e ordena por nome
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'escolinha/alunos.html', {'alunos': alunos})

