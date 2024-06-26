# Generated by Django 5.0.3 on 2024-04-24 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_orders_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower_design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flower_image', models.ImageField(blank=True, null=True, upload_to='flowers_design/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Greenery_design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greenery_design_image', models.ImageField(blank=True, null=True, upload_to='greenery_design/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packaging_design_image', models.ImageField(blank=True, null=True, upload_to='packaging_design/')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.orders')),
                ('flowers', models.ManyToManyField(blank=True, to='main.flower_design')),
                ('greenery', models.ManyToManyField(blank=True, to='main.greenery_design')),
                ('packaging', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.packaging')),
            ],
        ),
    ]
