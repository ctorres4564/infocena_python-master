from django.db import models


# Create your models here.
class MotivoContato(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class FaleConosco(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    motivoContato = models.ForeignKey(MotivoContato, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    assunto = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.nome} - {self.assunto[:30]}"


class Aluguel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefoneFixo = models.CharField(max_length=20)
    telefoneCelular = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} - {self.email}"


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} - {self.cpf}"
