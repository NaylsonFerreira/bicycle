# Generated by Django 4.0.4 on 2022-06-20 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0013_remove_notas_serie_rps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='codigo_verificacao',
        ),
        migrations.RemoveField(
            model_name='notas',
            name='nome_pdf',
        ),
        migrations.RemoveField(
            model_name='notas',
            name='rps',
        ),
    ]