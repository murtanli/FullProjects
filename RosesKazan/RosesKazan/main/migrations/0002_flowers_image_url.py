# Generated by Django 5.0.3 on 2024-04-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
