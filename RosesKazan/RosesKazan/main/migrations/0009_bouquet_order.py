# Generated by Django 5.0.3 on 2024-04-28 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_bouquet_order_cartitem_bouquet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.orders'),
        ),
    ]