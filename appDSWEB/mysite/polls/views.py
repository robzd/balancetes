from django.shortcuts import render, redirect, get_object_or_404
from .models import Balancete, Receita, Despesa
from .forms import BalanceteForm, ReceitaForm, DespesaForm, LoginForm, CadastroForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'polls/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('polls:menu') 
    else:
        form = LoginForm()
    
    return render(request, 'polls/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('polls:index')

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:login')
    else:
        form = CadastroForm()
    
    return render(request, 'polls/cadastro.html', {'form': form})

@login_required
def menu(request):
    username = request.user.username
    return render(request, 'polls/menu.html', {'username': username})

@login_required
def criarbalancete(request):
    if request.method == 'POST':
        form = BalanceteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:listarbalancetes')
    else:
        form = BalanceteForm()
    
    return render(request, 'polls/criarbalancete.html', {'form': form})

@login_required
def listarbalancetes(request):
    balancetes = Balancete.objects.all().order_by('-Data')
    return render(request, 'polls/listarbalancetes.html', {'balancetes': balancetes})

@login_required
def verbalancete(request, balancete_id):
    balancete = get_object_or_404(Balancete, id=balancete_id)

    searchquery = request.GET.get('search', '')

    receitasgeral = Receita.objects.filter(balancete=balancete)
    despesasgeral = Despesa.objects.filter(balancete=balancete)

    somareceitasgeral = sum(receita.Valor for receita in receitasgeral) or 0
    somadespesasgeral = sum(despesa.Valor for despesa in despesasgeral) or 0
    
    saldogeral = somareceitasgeral + somadespesasgeral

    receitas = receitasgeral.filter(Nome__icontains=searchquery)
    despesas = despesasgeral.filter(Nome__icontains=searchquery)
    
    somareceitas = sum(receita.Valor for receita in receitas) or 0
    somadespesas = sum(despesa.Valor for despesa in despesas) or 0
    
    saldoatual = somareceitas + somadespesas

    context = {
        'balancete': balancete,
        'receitas': receitas,
        'despesas': despesas,
        'saldoatual': saldoatual,
        'saldogeral': saldogeral,
        'searchquery': searchquery,
    }
    
    return render(request, 'polls/verbalancete.html', context)

@login_required
def addreceitadespesa(request, balancete_id):

    balancete = get_object_or_404(Balancete, id=balancete_id)

    if request.method == 'POST':
        if 'adicionarreceita' in request.POST:
            receitaform = ReceitaForm(request.POST)
            if receitaform.is_valid():
                receita = receitaform.save(commit=False)
                receita.balancete = balancete
                receita.save()
                return redirect('polls:verbalancete', balancete_id=balancete.id)
        elif 'adicionardespesa' in request.POST:
            despesaform = DespesaForm(request.POST)
            if despesaform.is_valid():
                despesa = despesaform.save(commit=False)
                despesa.balancete = balancete
                despesa.save()
                return redirect('polls:verbalancete', balancete_id=balancete.id)
    else:
        receitaform = ReceitaForm()
        despesaform = DespesaForm()

    return render(request, 'polls/addreceitadespesa.html', {
        'balancete': balancete,
        'receitaform': receitaform,
        'despesaform': despesaform
    })
