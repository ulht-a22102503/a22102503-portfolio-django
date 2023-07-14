from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
   
        # Para um conjunto de propriedade da classe (titulo, prioridade, concluido, etc), 
        # o dicionário widgets permite configurar o elemento HTML input correspondente, 
        # através de um dicionario de atributos de formatação (especificação de classes, placeholder, propriedades, etc).
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome do post'}),
        }


       # o dicionário labels especifica o texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
        }


       # o dicionário help_texts contém, para um atributo, um texto auxiliar a apresentar por baixo da janela de inserção
        #help_texts = {
        #    'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        #}
