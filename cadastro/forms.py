from django import forms

from cadastro.models import Loja


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
    
    