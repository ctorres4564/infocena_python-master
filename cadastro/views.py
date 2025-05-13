# START OF FILE views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# --- MODIFIED IMPORT START ---
from cadastro.forms import LojaForm, ProdutoForm
from .models import Loja, Produto

# --- MODIFIED IMPORT END ---

# Create your views here.


def index(request):
    # You might want to update this index later
    # return HttpResponse("Olá Mundo! Agora é web")
    # Example: render a simple index page for the cadastro app
    return render(request, "cadastro_index.html")  # Create this template


def listar_lojas(request):
    lojas = Loja.objects.order_by("nome")
    return render(request, "listar_lojas.html", {"lojas": lojas})


# cadastro/views.py


def incluir_loja(request):
    if request.method == "POST":
        form = LojaForm(request.POST)  # Cria form com dados submetidos
        if form.is_valid():
            form.save()
            return redirect("cadastro:listar_lojas")
    else:
        form = LojaForm()
    return render(request, "cadastro/incluir_loja.html", {"formulario": form})


def detalhar_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    return render(request, "detalhar_loja.html", {"loja": loja})


def alterar_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    if request.method == "POST":
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect("cadastro:listar_lojas")
    else:
        form = LojaForm(instance=loja)
    return render(request, "alterar_loja.html", {"formulario": form, "loja": loja})


def excluir_loja(request, id):
    loja = get_object_or_404(Loja, id=id)
    if request.method == "POST":
        loja.delete()
        return redirect("cadastro:listar_lojas")
    return render(request, "excluir_loja.html", {"loja": loja})


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "cadastro/listar_produtos.html", {"produtos": produtos})


def incluir_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastro:listar_produtos")
    else:
        form = ProdutoForm()
    return render(request, "cadastro/form_produto.html", {"form": form})


def detalhar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, "detalhar_produto.html", {"produto": produto})


def alterar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("cadastro:listar_produtos")
    else:
        form = ProdutoForm(instance=produto)
    return render(
        request, "alterar_produto.html", {"formulario": form, "produto": produto}
    )


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect("cadastro:listar_produtos")
    return render(request, "excluir_produto.html", {"produto": produto})


# --- ADDED CODE END ---


# END OF FILE views.py
