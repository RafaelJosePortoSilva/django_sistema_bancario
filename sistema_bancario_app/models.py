from django.db import models
from cpf_field.models import CPFField

# Create your models here.
class Conta(models.Model):
    saldo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    numero = models.IntegerField(
        primary_key=True,
        unique=True
    )

    agencia = models.IntegerField(

    )

    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE
    )

    historico = models.ForeignKey(
        'Historico',
        on_delete=models.CASCADE
    )


class ContaCorrente(models.Model):
    limite = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    limite_saques = models.IntegerField(

    )


class Cliente(models.Model):
    endereco = models.CharField(
        max_length=255
    )

    cpf = CPFField(
        unique=True
    )

    nome = models.CharField(
        max_length=255
    )

    data_nascimento = models.DateField(

    )


class Historico(models.Model):
    tipo_transacao = models.CharField(
        max_length=255,
        choices=[
            ('d', 'deposito'),
            ('s', 'saque')
        ]
    )

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


