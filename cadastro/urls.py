from django.urls import path
from . import views

app_name = "cadastro"

urlpatterns = [
    path("", views.index, name="index"),
    path("lojas/", views.listar_lojas, name="listar_lojas"),
    path("lojas/nova/", views.incluir_loja, name="incluir_loja"),
    path("lojas/<int:id>/", views.detalhar_loja, name="detalhar_loja"),
    path("lojas/<int:id>/editar/", views.alterar_loja, name="alterar_loja"),
    path("lojas/<int:id>/excluir/", views.excluir_loja, name="excluir_loja"),
    path("produtos/", views.listar_produtos, name="listar_produtos"),
    path("produtos/novo/", views.incluir_produto, name="incluir_produto"),
    path("produtos/<int:id>/", views.detalhar_produto, name="detalhar_produto"),
    path("produtos/<int:id>/editar/", views.alterar_produto, name="alterar_produto"),
    path("produtos/<int:id>/excluir/", views.excluir_produto, name="excluir_produto"),
]
