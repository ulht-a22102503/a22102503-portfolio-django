from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('blog/', views.blog_home_view, name='blog_home'),
    path('blog/new', views.blog_new_post_view, name='blog_new'),
    path('blog/edit/<int:post_id>', views.blog_edit_post_view, name='blog_edit'),
    path('blog/remove/<int:post_id>', views.blog_remove_post_view, name='blog_remove'),
    path('blog/<int:post_id>/like', views.blog_like_view, name='blog_like'),
    path('blog/<int:post_id>/dislike', views.blog_dislike_view, name='blog_dislike'),
    path('blog/<int:post_id>/comments/new', views.blog_comentario_new_view, name='blog_comentario_new'),
    path('cadeiras/home', views.cadeiras_home_view, name='cadeiras_home'),
    path('cadeiras/new/cadeira', views.cadeiras_new_view, name='cadeiras_new'),
    path('cadeiras/new/docente', views.docente_new_view, name='docentes_new'),
    path('labs/lab1', views.pwlab1_view, name='pwlab1'),
    path('labs/lab2', views.pwlab2_view, name='pwlab2'),
    path('labs/lab3', views.pwlab3_view, name='pwlab3'),
    path('labs/lab4', views.pwlab4_view, name='pwlab4'),
    path('projetos/home', views.projetos_home_view, name='projetos_home'),
    path('projetos/new', views.projetos_new_view, name='projetos_new'),
    path('tecnologias/home', views.tecnologias_home_view, name='tecnologias_home'),
    path('tecnologias/new', views.tecnologias_new_view, name='tecnologias_new'),
    path('webscraping/', views.web_scraping_view, name='web_scraping'),
    path('contacto/', views.contacto_view, name='contacto'),
]