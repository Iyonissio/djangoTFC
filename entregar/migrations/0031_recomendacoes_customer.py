# Generated by Django 3.0.7 on 2021-02-18 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entregar', '0030_auto_20201128_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendacoes',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='entregar.Customer'),
        ),
    ]
