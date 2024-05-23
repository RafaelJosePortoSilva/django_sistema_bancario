from django.contrib import admin
from sistema_bancario_app.models import Conta, ContaCorrente, Cliente, Historico

# Register your models here.
admin.site.register(Conta)
admin.site.register(ContaCorrente)
admin.site.register(Cliente)
admin.site.register(Historico)




