from django.shortcuts import render, redirect, get_object_or_404
from .models import Balancete, Receita, Despesa
from .forms import BalanceteForm, ReceitaForm, DespesaForm

def index(request):
    return render(request, 'polls/index.html')


def criarbalancete(request):
    if request.method == 'POST':
        form = BalanceteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:listarbalancetes')
    else:
        form = BalanceteForm()
    
    return render(request, 'polls/criarbalancete.html', {'form': form})

def listarbalancetes(request):
    balancetes = Balancete.objects.all().order_by('-baladata')
    return render(request, 'polls/listarbalancetes.html', {'balancetes': balancetes})

def verbalancete(request, balancete_id):
    balancete = get_object_or_404(Balancete, id=balancete_id)
    
    receitasgeral = Receita.objects.filter(balancete=balancete)
    despesasgeral = Despesa.objects.filter(balancete=balancete)
    
    somareceitasgeral = sum(receita.receitavalor for receita in receitasgeral)
    somadespesasgeral = sum(despesa.despesavalor for despesa in despesasgeral)
    saldogeral = somareceitasgeral - somadespesasgeral
    
    search_query = request.GET.get('search', '')
    receitas = receitasgeral.filter(receitanome__icontains=search_query)
    despesas = despesasgeral.filter(despesanome__icontains=search_query)
    
    somareceitas = sum(receita.receitavalor for receita in receitas)
    somadespesas = sum(despesa.despesavalor for despesa in despesas)
    saldoatual = somareceitas - somadespesas

    context = {
        'balancete': balancete,
        'receitas': receitas,
        'despesas': despesas,
        'saldoatual': saldoatual,
        'saldogeral': saldogeral,
        'search_query': search_query
    }
    
    return render(request, 'polls/verbalancete.html', context)

def addreceitadespesa(request, balancete_id):

    balancete = get_object_or_404(Balancete, id=balancete_id)

    if request.method == 'POST':
        if 'adicionar_receita' in request.POST:
            receita_form = ReceitaForm(request.POST)
            if receita_form.is_valid():
                receita = receita_form.save(commit=False)
                receita.balancete = balancete
                receita.save()
                return redirect('polls:verbalancete', balancete_id=balancete.id)
        elif 'adicionar_despesa' in request.POST:
            despesa_form = DespesaForm(request.POST)
            if despesa_form.is_valid():
                despesa = despesa_form.save(commit=False)
                despesa.balancete = balancete
                despesa.save()
                return redirect('polls:verbalancete', balancete_id=balancete.id)
    else:
        receita_form = ReceitaForm()
        despesa_form = DespesaForm()

    return render(request, 'polls/addreceitadespesa.html', {
        'balancete': balancete,
        'receita_form': receita_form,
        'despesa_form': despesa_form
    })
