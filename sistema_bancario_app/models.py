from django.db import models

# Create your models here.
class Conta(models.Model):

    saldo = models.DecimalField(
        max_digits=16,
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
        max_digits=16,
        decimal_places=2,
        default=0
    )

    limite_saques = models.IntegerField(

    )

class Cliente(models.Model):
    ...

class PessoaFisica(models.Model):
    ...

class Historico(models.Model):
    ...
