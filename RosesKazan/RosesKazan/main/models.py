from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)

class Flowers(models.Model):
    name = models.CharField(max_length=100)
    free_flowers = models.IntegerField()
    flower_image = models.ImageField(upload_to='flowers/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)

class Discount(models.Model):
    flower = models.ForeignKey(Flowers, models.CASCADE)
    discount_price = models.FloatField(null=True, blank=True)

class Orders(models.Model):
    status_list = (
        ('В сборке', 'В сборке'),
        ('Передается в доставку', 'Передается в доставку'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен')
    )

    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=status_list)
    order_date = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    flowers = models.ManyToManyField(Flowers, related_name='bookmarked_by')

class Stocks(models.Model):
    flower = models.ForeignKey(Flowers, null=True, blank=True, on_delete=models.CASCADE)
    stock_price = models.FloatField(max_length=20)

class CartItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    flower = models.ForeignKey(Flowers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)