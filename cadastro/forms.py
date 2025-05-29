from django import forms

from cadastro.models import Loja, Produto


class LojaForm(forms.ModelForm):
    nome = forms.CharField(label='Nome *',
                           error_messages={
                               'required': 'Campo Obrigatório'
                           })
    telefone = forms.CharField(label='Telefone *',
                           error_messages={
                               'required': 'Campo Obrigatório'
                           })
    class Meta:
        model = Loja
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(label="Nome do Produto ")
    preco = forms.DecimalField(label="Preço ")
    destaque = forms.BooleanField(label="Aparecer no site")
    class Meta:
        model = Produto
        fields = '__all__'
    
    