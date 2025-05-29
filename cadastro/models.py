from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    numero = models.CharField(max_length = 5, 
                              null=True, 
                              blank=True)

    def __str__(self):
        return f"{self.nome} - {self.telefone}" 

class Produto(models.Model):
    loja = models.ForeignKey(Loja, 
                    on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, 
                                decimal_places=2)
    destaque = models.BooleanField() 

    def __str__(self):
        return f"{self.nome} - {self.preco}"
    '''
    dçdçdç
    ssçsçsç
    '''