from django.db import models

# Create your models here.
class Conta(models.Model):

    saldo = models.DecimalField(
        max_digits=16,
        decimal_places=2
    )

class ContaCorrente(models.Model):
    ...

class Cliente(models.Model):
    ...

class PessoaFisica(models.Model):
    ...

class Historico(models.Model):
    ...
