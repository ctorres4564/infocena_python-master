from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FaleConosco, Aluguel, Cliente, MotivoContato
from .forms import FaleConoscoForm, AluguelForm, ClienteForm


# Create your views here.
def index(request):
    return render(request, "index.html")


def quem_somos(request):
    return render(request, "quem_somos.html")


# Views para FaleConosco
def fale_conosco_list(request):
    contatos = FaleConosco.objects.all().order_by("-id")
    return render(request, "fale_conosco/list.html", {"contatos": contatos})


def fale_conosco_create(request):
    if request.method == "POST":
        form = FaleConoscoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect("fale_conosco_list")
    else:
        form = FaleConoscoForm()
    return render(request, "fale_conosco.html", {"form": form})


# Views para Aluguel
def aluguel_list(request):
    alugueis = Aluguel.objects.all().order_by("-id")
    return render(request, "aluguel/list.html", {"alugueis": alugueis})


def aluguel_create(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Solicitação de aluguel registrada com sucesso!")
            return redirect("aluguel_list")
    else:
        form = AluguelForm()
    return render(request, "aluguel.html", {"form": form})


# Views para Cliente
def cliente_list(request):
    clientes = Cliente.objects.all().order_by("-id")
    return render(request, "cliente/list.html", {"clientes": clientes})


def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        Cliente.objects.create(nome=nome, cpf=cpf, email=email, telefone=telefone)
        messages.success(request, "Cliente cadastrado com sucesso!")
        return redirect("cliente_list")

    return render(request, "cliente/create.html")


def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.nome = request.POST.get("nome")
        cliente.cpf = request.POST.get("cpf")
        cliente.email = request.POST.get("email")
        cliente.telefone = request.POST.get("telefone")
        cliente.save()
        messages.success(request, "Cliente atualizado com sucesso!")
        return redirect("cliente_list")

    return render(request, "cliente/edit.html", {"cliente": cliente})


def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso!")
        return redirect("cliente_list")

    return render(request, "cliente/delete.html", {"cliente": cliente})
