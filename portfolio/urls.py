from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.layout_view, name='index'),
    path('home/', views.discoparty_view, name='discoparty'),
    path('random/', views.random_view, name='random'),
]