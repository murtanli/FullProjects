# Generated by Django 5.0.3 on 2024-04-28 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_bouquet_flowers_alter_bouquet_greenery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bouquet',
            name='order',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='bouquet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.bouquet'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='flower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.flowers'),
        ),
    ]
