from django import forms
from django.forms import ModelForm
from .models import Post, Comentario, Projeto, Tecnologia, Contacto

#Blog
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
   
        # Para um conjunto de propriedade da classe (titulo, prioridade, concluido, etc), 
        # o dicionário widgets permite configurar o elemento HTML input correspondente, 
        # através de um dicionario de atributos de formatação (especificação de classes, placeholder, propriedades, etc).
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome do post'}),
            'descricao': forms.Textarea,
        }


       # o dicionário labels especifica o texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
        }

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'

        widgets = {
            'texto': forms.Textarea
        }

        labels = {
            'name':'Nome',
            'email': 'Email de contacto',
            'subject': 'Assunto',
            'message': 'Mensagem',
        }

class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'descricao': forms.Textarea
        }

        labels = {
            'name':'Nome',
            'repo_link': 'Link do repositório',
            'descricao': 'Descrição',
        }

class TecnologiaForm(ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

        widgets = {
            'descricao': forms.Textarea
        }

        labels = {
            'name':'Nome',
            'website': 'Link do projeto',
            'repo_link': 'Link do repositório',
            'descricao': 'Descrição',
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
            'message': forms.Textarea
        }

        labels = {
            'name':'Nome',
            'email': 'Email de contacto',
            'subject': 'Assunto',
            'message': 'Mensagem',
        }