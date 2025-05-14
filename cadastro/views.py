from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


from cadastro.forms import LojaForm, ProdutoForm
from .models import Loja, Produto


def index(request):
    return render(request, "cadastro/cadastro_index.html")


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


def listar_produtos(request, id_loja):
    loja = get_object_or_404(Loja, id=id_loja)
    produtos = Produto.objects.filter(loja=loja).order_by("nome")
    return render(
        request,
        "cadastro/listar_produtos_por_loja.html",
        {"produtos": produtos, "loja": loja},
    )


def incluir_produto(request, id_loja):
    loja = get_object_or_404(Loja, id=id_loja)
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.loja = loja
            produto.save()
            return redirect("cadastro:listar_produtos", id_loja=loja.id)
    else:
        form = ProdutoForm()
    return render(request, "cadastro/form_produto.html", {"form": form, "loja": loja})


def detalhar_produto(request, id_loja, id_produto):
    loja = get_object_or_404(Loja, id=id_loja)
    produto = get_object_or_404(Produto, id=id_produto, loja=loja)
    return render(
        request, "cadastro/detalhar_produto.html", {"produto": produto, "loja": loja}
    )


def alterar_produto(request, id_loja, id_produto):
    loja = get_object_or_404(Loja, id=id_loja)
    produto = get_object_or_404(Produto, id=id_produto, loja=loja)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect("cadastro:listar_produtos", id_loja=loja.id)
    else:
        form = ProdutoForm(instance=produto)
    return render(
        request,
        "cadastro/alterar_produto.html",
        {"formulario": form, "produto": produto, "loja": loja},
    )


def excluir_produto(request, id_loja, id_produto):
    loja = get_object_or_404(Loja, id=id_loja)
    produto = get_object_or_404(Produto, id=id_produto, loja=loja)
    if request.method == "POST":
        produto.delete()
        return redirect("cadastro:listar_produtos", id_loja=loja.id)
    return render(
        request, "cadastro/excluir_produto.html", {"produto": produto, "loja": loja}
    )


# --- ADDED CODE END ---


# END OF FILE views.py
