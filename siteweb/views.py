from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Área Institucional (Pública)
def index(request):
    return render(request, 'siteweb/index.html')

def sobre(request):
    return render(request, 'siteweb/sobre.html')

def contato(request):
    return render(request, 'siteweb/contato.html')

def produtos_publicos(request):
    return render(request, 'siteweb/produtos_publicos.html')

# Área Interna (Privada)
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'siteweb/admin/dashboard.html')

@login_required(login_url='login')
def produtos_admin(request):
    return render(request, 'siteweb/admin/produtos.html')

@login_required(login_url='login')
def usuarios(request):
    return render(request, 'siteweb/admin/usuarios.html')

@login_required(login_url='login')
def relatorios(request):
    return render(request, 'siteweb/admin/relatorios.html')
