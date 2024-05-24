from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Conta, Historico
from sistema_bancario_app.forms import ContaForm, ClienteForm


def index(request, conta_id):
    conta = get_object_or_404(Conta, numero=conta_id)
    historico = conta.historicos.all().order_by('-data')
    return render(request, 'index.html', {'conta': conta, 'historico': historico})

@csrf_protect
def fazer_transacao(request, conta_id):
    conta = get_object_or_404(Conta, numero=conta_id)
    if request.method == 'POST':
        tipo = request.POST['tipo']
        valor = float(request.POST['valor'])
        
        if tipo == 's' and valor > conta.saldo:
            # Adicionar mensagem de erro (saldo insuficiente)
            return redirect('index', conta_id=conta_id)
        
        if tipo == 'd':
            conta.saldo += valor
        elif tipo == 's':
            conta.saldo -= valor
        
        conta.save()
        
        Historico.objects.create(tipo_transacao=tipo, valor=valor, conta=conta)
        return redirect('index', conta_id=conta_id)
    
    return redirect('index', conta_id=conta_id)

def criar_conta(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        conta_form = ContaForm(request.POST)
        
        if cliente_form.is_valid() and conta_form.is_valid():
            cliente = cliente_form.save()
            conta = conta_form.save(commit=False)
            conta.cliente = cliente
            conta.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm()
        conta_form = ContaForm()

    return render(request, 'criar_conta.html', {'cliente_form': cliente_form, 'conta_form': conta_form})