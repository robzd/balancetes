from django import forms
from .models import Balancete, Receita, Despesa

class BalanceteForm(forms.ModelForm):
    class Meta:
        model = Balancete
        fields = ['balanome', 'baladata', 'balafoto']
        widgets = {
            'baladata': forms.DateInput(attrs={'type': 'date'}),
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['receitanome','receitavalor']
        widgets = {
            'receitavalor': forms.NumberInput(attrs={'min': 0}),
        }

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['despesanome','despesavalor']
        widgets = {
            'despesavalor': forms.NumberInput(attrs={'max': 0}),
        }