# Generated by Django 5.0.3 on 2024-04-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
