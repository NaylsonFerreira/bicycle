# Generated by Django 4.0.4 on 2022-06-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_rename_cnpjcpf_pres_notas_cnpjcpf_prest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notas',
            name='cancelada',
            field=models.CharField(max_length=2),
        ),
    ]