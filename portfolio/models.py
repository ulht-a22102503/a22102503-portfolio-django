from django.db import models

# Create your models here.

# Blog
class Post(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=2000)
    link = models.URLField(max_length=100, blank=True, null=True)
    imagem = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.titulo[:20]

#Contacto
class Contacto(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=1024)
    message = models.TextField()

    def __str__(self):
        return self.email

#Projeto
class Projeto(models.Model):
    name = models.CharField(max_length=150)
    repo_link = models.URLField(max_length=500)
    descricao = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

#Tecnologia


#Unidade Curricular