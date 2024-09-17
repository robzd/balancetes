from django.db import models

class Balancete(models.Model):
    balanome = models.CharField(max_length=100)
    baladata = models.DateField("Data de Publicação:")
    balafoto = models.ImageField(upload_to='balancetes/', null=True, blank=True)
    
class Receita(models.Model):
    balancete = models.ForeignKey(Balancete, default=0, on_delete=models.CASCADE)
    receitanome = models.CharField(max_length=100)
    receitavalor = models.IntegerField(default=0)
    
class Despesa(models.Model):
    balancete = models.ForeignKey(Balancete, default=0, on_delete=models.CASCADE)
    despesanome = models.CharField(max_length=100)
    despesavalor = models.IntegerField(default=0)
