from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('blog/', views.blog_home_view, name='blog_home'),
    path('blog/new', views.blog_new_post_view, name='blog_new'),
    path('blog/edit/<int:post_id>', views.blog_edit_post_view, name='blog_edit'),
    path('blog/remove/<int:post_id>', views.blog_remove_post_view, name='blog_remove'),
    path('labs/lab1', views.pwlab1_view, name='pwlab1'),
    path('labs/lab2', views.pwlab2_view, name='pwlab2'),
    path('labs/lab3', views.pwlab3_view, name='pwlab3'),
    path('labs/lab4', views.pwlab4_view, name='pwlab4'),
    path('contacto/', views.contacto_view, name='contacto'),
]