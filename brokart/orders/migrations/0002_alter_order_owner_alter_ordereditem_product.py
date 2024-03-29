# Generated by Django 5.0.2 on 2024-02-15 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('orders', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='customer.customers'),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='product.products'),
        ),
    ]
