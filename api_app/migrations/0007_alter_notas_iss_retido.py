# Generated by Django 4.0.4 on 2022-06-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0006_alter_notas_aliq_iss_alter_notas_codigo_servico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='iss_retido',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
