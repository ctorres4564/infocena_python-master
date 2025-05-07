from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from cadastro.forms import LojaForm
from .models import Loja

# Create your views here.

def index(request):
    return HttpResponse("Olá Mundo! Agora é web")

def listar_lojas(request):
    lojas = Loja.objects.order_by('nome')
    return render(request, 'listar_lojas.html',
                  {'lojas':lojas })

def incluir_loja(request):
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro:listar_lojas')
    form = LojaForm()
    return render(request, 'incluir_loja.html',
                  {'formulario': form})

def detalhar_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    return render(request, 'detalhar_loja.html', {'loja': loja})

def alterar_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect('cadastro:listar_lojas')
    form = LojaForm(instance=loja)
    return render(request, 'alterar_loja.html', {'formulario': form, 'loja': loja})

def excluir_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    if request.method == 'POST':
        loja.delete()
        return redirect('cadastro:listar_lojas')
    return render(request, 'excluir_loja.html', {'loja': loja})

            

