from django import forms
from .models import FaleConosco, Aluguel, Cliente


class FaleConoscoForm(forms.ModelForm):
    class Meta:
        model = FaleConosco
        fields = ["nome", "email", "motivoContato", "telefone", "assunto"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "motivoContato": forms.Select(attrs={"class": "form-select"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "assunto": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ["nome", "email", "telefoneFixo", "telefoneCelular"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefoneFixo": forms.TextInput(attrs={"class": "form-control"}),
            "telefoneCelular": forms.TextInput(attrs={"class": "form-control"}),
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf", "email", "telefone"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
        }
