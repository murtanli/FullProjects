from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class Profile(models.Model):
    user = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    email = models.CharField(max_length=50)

class Flowers(models.Model):
    name = models.CharField(max_length=100)
    free_flowers = models.IntegerField()
    flower_image = models.ImageField(upload_to='flowers/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)
class Orders(models.Model):
    status_list = (
        ('В сборке', 'В сборке'),
        ('Передается в доставку', 'Передается в доставку'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен')
    )

    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status_list)
    order_date = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    flowers = models.ManyToManyField(Flowers, related_name='bookmarked_by')

class Stocks(models.Model):
    flower = models.ForeignKey(Flowers, null=True, blank=True, on_delete=models.CASCADE)
    stock_price = models.FloatField(max_length=20)
