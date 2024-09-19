from django.db import models

class Balancete(models.Model):
    Nome = models.CharField(max_length=100)
    Data = models.DateField("Data de Publicação:")
    Foto = models.ImageField(upload_to='balancetes/', null=True, blank=True)
    
class Receita(models.Model):
    balancete = models.ForeignKey(Balancete, default=0, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=100)
    Valor = models.IntegerField(default=0)
    
class Despesa(models.Model):
    balancete = models.ForeignKey(Balancete, default=0, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=100)
    Valor = models.IntegerField(default=0)
