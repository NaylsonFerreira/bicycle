# Generated by Django 4.0.4 on 2022-06-20 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0019_alter_notas_cancelada_alter_notas_codigo_servico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='rps',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]