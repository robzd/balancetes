# Generated by Django 4.2.16 on 2024-09-18 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_balancete_balafoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balancete',
            old_name='balanome',
            new_name='Nome',
        ),
    ]
