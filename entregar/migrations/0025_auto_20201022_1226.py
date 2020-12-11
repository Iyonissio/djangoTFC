# Generated by Django 3.0.7 on 2020-10-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entregar', '0024_auto_20201022_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco_a_pagar', models.IntegerField(max_length=200, null=True)),
                ('forma_pagamento', models.CharField(choices=[('PayPal', 'PayPal'), ('PayPal', 'PayPal')], max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Notas_Pedido',
        ),
    ]
