# Generated by Django 4.2.16 on 2024-09-20 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balancete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Data', models.DateField(verbose_name='Data de Publicação:')),
                ('Foto', models.ImageField(blank=True, null=True, upload_to='balancetes/')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Valor', models.IntegerField(default=0)),
                ('balancete', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.balancete')),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Valor', models.IntegerField(default=0)),
                ('balancete', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='polls.balancete')),
            ],
        ),
    ]
