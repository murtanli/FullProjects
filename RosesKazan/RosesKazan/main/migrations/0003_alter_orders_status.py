# Generated by Django 5.0.3 on 2024-04-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_orders_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('В сборке', 'В сборке'), ('Передается в доставку', 'Передается в доставку'), ('В пути', 'В пути'), ('Доставлен', 'Доставлен'), ('Получен', 'Получен')], max_length=50),
        ),
    ]
