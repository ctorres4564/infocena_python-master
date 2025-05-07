from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.index, name='index'),
    
    # URLs para gerenciamento de lojas
    path('lojas/', views.listar_lojas, name='listar_lojas'),
    path('lojas/nova/', views.incluir_loja, name='incluir_loja'),
    path('lojas/<int:id>/', views.detalhar_loja, name='detalhar_loja'),
    path('lojas/<int:id>/editar/', views.alterar_loja, name='alterar_loja'),
    path('lojas/<int:id>/excluir/', views.excluir_loja, name='excluir_loja'),
]

