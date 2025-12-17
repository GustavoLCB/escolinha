from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# ADICIONEI 'localizacao' e 'contato' NA IMPORTAÇÃO ABAIXO:
from escolinha.views import index, professores, valores, metodologia, lista_alunos, localizacao, contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('professores/', professores, name='professores'),
    path('valores/', valores, name='valores'),
    path('metodologia/', metodologia, name='metodologia'),
    path('localizacao/', localizacao, name='localizacao'),
    path('contato/', contato, name='contato'),
    path('login/', auth_views.LoginView.as_view(template_name='escolinha/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('alunos/', lista_alunos, name='lista_alunos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
