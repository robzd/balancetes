from django import forms
from .models import Balancete, Receita, Despesa
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=20)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class CadastroForm(forms.ModelForm):
    username = forms.CharField(
        max_length=20,
        required=True,
        error_messages={'required': '', 'max_length': ''}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=True,
        error_messages={'required': ''} 
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    

class BalanceteForm(forms.ModelForm):
    class Meta:
        model = Balancete
        fields = ['Nome', 'Data', 'Foto']
        widgets = {
            'Data': forms.DateInput(attrs={'type': 'date'}),
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['Nome', 'Valor']
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'Nome'}),
            'Valor': forms.NumberInput(attrs={'class': 'Valor', 'min': 0}),
        }

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['Nome', 'Valor']
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'Nome'}),
            'Valor': forms.NumberInput(attrs={'class': 'Valor', 'max': 0}),
        }
