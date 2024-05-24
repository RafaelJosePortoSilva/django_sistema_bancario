# forms.py

from django import forms
from .models import Cliente, Conta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['endereco', 'cpf', 'nome', 'data_nascimento']

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['numero', 'agencia', 'saldo']
