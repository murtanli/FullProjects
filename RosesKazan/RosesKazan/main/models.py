from django.db import models
from django.contrib.auth.models import User



class Flower_design(models.Model):
    flower_image = models.ImageField(upload_to='flowers_design/', blank=True, null=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Greenery_design(models.Model):
    greenery_design_image = models.ImageField(upload_to='greenery_design/', blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Packaging(models.Model):
    packaging_design_image = models.ImageField(upload_to='packaging_design/', blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)



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
        ('На месте', 'На месте'),
        ('Получен', 'Получен')
    )

    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=status_list)
    order_date = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    #flowers = models.ManyToManyField(Flowers, related_name='bookmarked_by', null=True, blank=True)
class Bouquet(models.Model):
    order = models.ForeignKey(Orders, null=True, blank=True, on_delete=models.CASCADE)
    flowers = models.ManyToManyField(Flower_design, blank=True, null=True)
    greenery = models.ManyToManyField(Greenery_design, blank=True, null=True)
    packaging = models.ForeignKey(Packaging,on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
class OrderFlower(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flowers, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Stocks(models.Model):
    flower = models.ForeignKey(Flowers, null=True, blank=True, on_delete=models.CASCADE)
    stock_price = models.FloatField(max_length=20)

class CartItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    flower = models.ForeignKey(Flowers, on_delete=models.CASCADE, null=True, blank=True)
    bouquet = models.ForeignKey(Bouquet, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)


