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
    path('labs/lab1', views.pwlab1_view, name='pwlab1'),
    path('labs/lab2', views.pwlab2_view, name='pwlab2'),
    path('labs/lab3', views.pwlab3_view, name='pwlab3'),
    path('labs/lab4', views.pwlab4_view, name='pwlab4'),
    path('projetos/home', views.projetos_home_view, name='projetos_home'),
    path('projetos/new', views.projetos_new_view, name='projetos_new'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('webscraping/', views.web_scraping_view, name='web_scraping'),
]