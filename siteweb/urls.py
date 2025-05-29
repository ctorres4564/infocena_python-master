from django.urls import path

from siteweb import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quem_somos", views.quem_somos, name="quem_somos"),
    # URLs para FaleConosco
    path("fale-conosco/", views.fale_conosco_list, name="fale_conosco_list"),
    path("fale-conosco/criar/", views.fale_conosco_create, name="fale_conosco_create"),
    # URLs para Aluguel
    path("aluguel/", views.aluguel_list, name="aluguel_list"),
    path("aluguel/criar/", views.aluguel_create, name="aluguel_create"),
    # URLs para Cliente
    path("clientes/", views.cliente_list, name="cliente_list"),
    path("clientes/criar/", views.cliente_create, name="cliente_create"),
    path("clientes/editar/<int:pk>/", views.cliente_edit, name="cliente_edit"),
    path("clientes/excluir/<int:pk>/", views.cliente_delete, name="cliente_delete"),
]
