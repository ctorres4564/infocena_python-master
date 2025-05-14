from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "cadastro"

urlpatterns = [
    path("", views.index, name="index"),
    path("lojas/", views.listar_lojas, name="listar_lojas"),
    path("lojas/nova/", views.incluir_loja, name="incluir_loja"),
    path("lojas/<int:id>/", views.detalhar_loja, name="detalhar_loja"),
    path("lojas/<int:id>/editar/", views.alterar_loja, name="alterar_loja"),
    path("lojas/<int:id>/excluir/", views.excluir_loja, name="excluir_loja"),
    # URLs de Produtos aninhadas sob Loja
    path(
        "loja/<int:id_loja>/produtos/",
        views.listar_produtos,
        name="listar_produtos",
    ),
    path(
        "loja/<int:id_loja>/produtos/novo/",
        views.incluir_produto,
        name="incluir_produto",
    ),
    path(
        "loja/<int:id_loja>/produtos/<int:id_produto>/",
        views.detalhar_produto,
        name="detalhar_produto",
    ),
    path(
        "loja/<int:id_loja>/produtos/<int:id_produto>/alterar/",
        views.alterar_produto,
        name="alterar_produto",
    ),
    path(
        "loja/<int:id_loja>/produtos/<int:id_produto>/excluir/",
        views.excluir_produto,
        name="excluir_produto",
    ),
    path('login/', auth_views.LoginView.as_view(template_name='cadastro/login.html'), name='login'),
    path('area-interna/', views.area_interna, name='area_interna'),
]
