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
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.CharField(max_length=20)
    texto = models.CharField(max_length=2000)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.postID} {self.data}'

#Contacto
class Contacto(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=1024)
    message = models.TextField()

    def __str__(self):
        return self.email

#Tecnologia
class Tecnologia(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(max_length=500)
    source_code = models.URLField(max_length=500)
    descricao = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

#Projeto
class Projeto(models.Model):
    name = models.CharField(max_length=150)
    repo_link = models.URLField(max_length=500)
    descricao = models.CharField(max_length=2000)
    #tecnologias = models.ForeignKey(Tecnologia, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#Unidade Curricular