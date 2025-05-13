
from django.db import models


class Loja(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    numero = models.CharField(max_length = 5,
                              null=True,
                              blank=True)

    def __str__(self):
        return f"{self.nome} - {self.telefone}"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='produtos', null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"