# Generated by Django 5.0.3 on 2024-04-27 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_flower_design_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='flowers',
            field=models.ManyToManyField(blank=True, null=True, to='main.flower_design'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='greenery',
            field=models.ManyToManyField(blank=True, null=True, to='main.greenery_design'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.orders'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='packaging',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.packaging'),
        ),
    ]
