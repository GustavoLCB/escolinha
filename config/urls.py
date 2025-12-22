from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# ADICIONEI 'localizacao' e 'contato' NA IMPORTAÇÃO ABAIXO:
from escolinha.views import (
    index, professores, valores, metodologia, lista_alunos, localizacao, contato, 
    editar_aluno, deletar_aluno, criar_aluno,
    criar_professor, editar_professor, deletar_professor,
    criar_plano, editar_plano, deletar_plano,
    lista_turmas, criar_turma, editar_turma, deletar_turma,
)

urlpatterns = [
    path('gestao-super-secreta-2011/', admin.site.urls),
    path('', index, name='home'),
    path('professores/', professores, name='professores'),
    path('professores/novo/', criar_professor, name='criar_professor'),
    path('professores/editar/<int:id>/', editar_professor, name='editar_professor'),
    path('professores/deletar/<int:id>/', deletar_professor, name='deletar_professor'),
    path('valores/', valores, name='valores'),
    path('planos/novo/', criar_plano, name='criar_plano'),
    path('planos/editar/<int:id>/', editar_plano, name='editar_plano'),
    path('planos/deletar/<int:id>/', deletar_plano, name='deletar_plano'),
    path('metodologia/', metodologia, name='metodologia'),
    path('localizacao/', localizacao, name='localizacao'),
    path('contato/', contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='escolinha/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('alunos/', lista_alunos, name='lista_alunos'),
    path('alunos/novo/', criar_aluno, name='criar_aluno'),
    path('alunos/editar/<int:id>/', editar_aluno, name='editar_aluno'),
    path('alunos/deletar/<int:id>/', deletar_aluno, name='deletar_aluno'),
    path('turmas/', lista_turmas, name='lista_turmas'),
    path('turmas/nova/', criar_turma, name='criar_turma'),
    path('turmas/editar/<int:id>/', editar_turma, name='editar_turma'),
    path('turmas/deletar/<int:id>/', deletar_turma, name='deletar_turma'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
