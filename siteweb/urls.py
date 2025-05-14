from django.urls import path
from django.contrib.auth import views as auth_views
from siteweb import views

urlpatterns = [
    # Área Institucional (Pública)
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('produtos/', views.produtos_publicos, name='produtos_publicos'),
    
    # Área Interna (Privada)
    path('admin/login/', auth_views.LoginView.as_view(template_name='siteweb/login.html'), name='login'),
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('admin/dashboard/', views.dashboard, name='dashboard'),
    path('admin/produtos/', views.produtos_admin, name='produtos_admin'),
    path('admin/usuarios/', views.usuarios, name='usuarios'),
    path('admin/relatorios/', views.relatorios, name='relatorios'),
]