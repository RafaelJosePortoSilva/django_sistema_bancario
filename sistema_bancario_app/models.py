# models.py

from django.db import models
from cpf_field.models import CPFField

class Cliente(models.Model):
    endereco = models.CharField(max_length=255)
    cpf = CPFField(unique=True)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()

class Conta(models.Model):
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    numero = models.IntegerField(primary_key=True, unique=True)
    agencia = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Historico(models.Model):
    TIPO_TRANSACAO_CHOICES = [
        ('d', 'Depósito'),
        ('s', 'Saque'),
    ]
    tipo_transacao = models.CharField(max_length=1, choices=TIPO_TRANSACAO_CHOICES)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='historicos', null=True)  # Permitir nulo temporariamente

class ContaCorrente(models.Model):
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE, null=True)
    limite = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    limite_saques = models.IntegerField()

