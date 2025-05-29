from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('listar_lojas', views.listar_lojas, 
            name='listar_lojas'),
            
    path('incluir_loja', views.incluir_loja,
            name='incluir_loja'),   

    path('alterar_loja/<int:codigo>', views.alterar_loja,
            name='alterar_loja'),   

    path('excluir_loja/<int:codigo>', views.excluir_loja,
            name='excluir_loja'), 

    path('listar_produtos', views.listar_produtos,
           name='listar_produtos'),
    path('incluir_produto', views.incluir_produto,
           name='incluir_produto'), 
    path('alterar_produto/<int:codigo>', 
                views.alterar_produto,
                name='alterar_produto'),               
    path('excluir_produto/<int:codigo>', 
                views.excluir_produto,
                name='excluir_produto'),    

    path('area_interna', views.area_interna,
         name='area_interna'),    
]

