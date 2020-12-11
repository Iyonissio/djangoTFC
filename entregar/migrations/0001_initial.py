# Generated by Django 3.0.7 on 2020-10-10 00:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='SemFT.png', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mesas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('categoria', models.CharField(choices=[('EMPRESARIAL', 'EMPRESARIAL'), ('SOCIAL', 'SOCIAL'), ('CASAL', 'CASAL')], max_length=15)),
                ('cadeiras', models.IntegerField()),
                ('capacidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('Levar', 'Levar'), ('Entregar ; Delivery', 'Entregar ; Delivery ')], max_length=200)),
                ('description', models.TextField(blank=True, max_length=134500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='recomendacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reclamacao', models.TextField(blank=True, max_length=5000, null=True)),
                ('recomendacao', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField()),
                ('saida', models.DateTimeField()),
                ('nome_da_reserva', models.CharField(max_length=200, null=True)),
                ('nr_de_pessoas', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entregar.Customer')),
                ('mesas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entregar.Mesas')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adicionar_Ingrediente', models.CharField(max_length=200, null=True)),
                ('remover_Ingrediente', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Pronto em 30min', 'Pronto em 30min'), ('Pronto em 15min', 'Pronto em 15min'), ('Pronto em 5min', 'Pronto em 5min'), ('Saiu Para Entrega', 'Saiu Para Entrega'), ('Entregue', 'Entregue')], max_length=200, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entregar.Customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entregar.Product')),
            ],
        ),
    ]