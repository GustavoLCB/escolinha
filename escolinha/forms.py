from django import forms
from .models import Aluno, Professor, Plano, Turma

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'telefone', 'ano_nascimento', 'observacoes']
        # Aqui deixamos os campos bonitos com classes CSS
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_nascimento': forms.NumberInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'especialidade', 'foto', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'class': 'form-control'}),
            # Foto não precisa de widget específico, o Django cuida
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        # Adicionei 'periodo' na lista de campos
        fields = ['titulo', 'subtitulo', 'preco', 'periodo', 'beneficios']
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            
            # Widget Select para criar o menu de opções
            'periodo': forms.Select(attrs={'class': 'form-control'}),
            
            'beneficios': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'dias', 'horario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Sub-09 Manhã'}),
            'dias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Seg e Qua'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 09:00 - 10:30'}),
        }