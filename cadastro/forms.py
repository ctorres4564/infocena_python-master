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
    imagem = forms.ImageField(label='Imagem', required=False)
    class Meta:
        model = Loja
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome *',
                           error_messages={
                               'required': 'Campo Obrigatório'
                           })
    preco = forms.DecimalField(label='Preço *',
                               max_digits=10,
                               decimal_places=2,
                               error_messages={
                                   'required': 'Campo Obrigatório'
                               })
    estoque = forms.IntegerField(label='Estoque', required=False, initial=0)
    descricao = forms.CharField(label='Descrição', required=False, widget=forms.Textarea)
    imagem = forms.ImageField(label='Imagem', required=False)

    class Meta:
        model = Produto
        fields = '__all__'

