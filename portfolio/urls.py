from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('home/', views.discoparty_view, name='discoparty'),
    path('blog/', views.blog_home_view, name='blog_home'),
    path('blog/new', views.blog_new_post_view, name='blog_new'),
    path('blog/edit/<int:post_id>', views.blog_edit_post_view, name='blog_edit'),
    path('blog/remove/<int:post_id>', views.blog_remove_post_view, name='blog_remove'),
    path('random/', views.random_view, name='random'),
]