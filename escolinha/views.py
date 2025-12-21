from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # Importação de segurança
from .models import Professor, Plano, Aluno, Turma # Importamos os modelos
from .forms import AlunoForm, ProfessorForm, PlanoForm, TurmaForm

def index(request):
    # Busca todas as turmas cadastradas no banco
    turmas = Turma.objects.all()
    return render(request, 'escolinha/index.html', {'turmas': turmas})

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

def localizacao(request):
    return render(request, 'escolinha/localizacao.html')

def contato(request):
    return render(request, 'escolinha/contato.html')

@login_required
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    
    return render(request, 'escolinha/aluno_form.html', {'form': form, 'aluno': aluno})

@login_required
def deletar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    
    return render(request, 'escolinha/aluno_confirm_delete.html', {'aluno': aluno})

@login_required
def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm() # Formulário vazio
    
    # Vamos reutilizar o template de formulário
    return render(request, 'escolinha/aluno_form.html', {'form': form})

@login_required
def criar_professor(request):
    if request.method == 'POST':
        # ATENÇÃO: request.FILES é obrigatório para salvar fotos!
        form = ProfessorForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('professores')
    else:
        form = ProfessorForm()
    return render(request, 'escolinha/professor_form.html', {'form': form})

@login_required
def editar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    if request.method == 'POST':
        # request.FILES aqui também para atualizar a foto se precisar
        form = ProfessorForm(request.POST, request.FILES, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professores')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'escolinha/professor_form.html', {'form': form, 'professor': professor})

@login_required
def deletar_professor(request, id):
    professor = get_object_or_404(Professor, id=id)
    if request.method == 'POST':
        professor.delete()
        return redirect('professores')
    return render(request, 'escolinha/professor_confirm_delete.html', {'professor': professor})

@login_required
def criar_plano(request):
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('valores')
    else:
        form = PlanoForm()
    return render(request, 'escolinha/plano_form.html', {'form': form})

@login_required
def editar_plano(request, id):
    plano = get_object_or_404(Plano, id=id)
    if request.method == 'POST':
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            form.save()
            return redirect('valores')
    else:
        form = PlanoForm(instance=plano)
    return render(request, 'escolinha/plano_form.html', {'form': form})

@login_required
def deletar_plano(request, id):
    plano = get_object_or_404(Plano, id=id)
    if request.method == 'POST':
        plano.delete()
        return redirect('valores')
    return render(request, 'escolinha/plano_confirm_delete.html', {'plano': plano})

# --- CRUD TURMAS ---

def lista_turmas(request):
    turmas = Turma.objects.all()
    return render(request, 'escolinha/turmas.html', {'turmas': turmas})

@login_required
def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_turmas')
    else:
        form = TurmaForm()
    return render(request, 'escolinha/turma_form.html', {'form': form})

@login_required
def editar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    if request.method == 'POST':
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            return redirect('lista_turmas')
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'escolinha/turma_form.html', {'form': form})

@login_required
def deletar_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    if request.method == 'POST':
        turma.delete()
        return redirect('lista_turmas')
    return render(request, 'escolinha/turma_confirm_delete.html', {'turma': turma})