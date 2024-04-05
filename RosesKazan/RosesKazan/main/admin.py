from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'login', 'password')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'flower', 'discount_price')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'name', 'lastname', 'email')

@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','category', 'free_flowers', 'flower_image','image_preview', 'price')

    def image_preview(self, obj):
        # Отображение изображения в админке
        if obj.flower_image:
            flower_id = obj.pk
            url = reverse('get_flower_image', args=[flower_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    image_preview.short_description = 'Image Preview'

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile', 'order_number', 'address', 'status', 'order_date', 'arrival_time', 'price', 'display_flowers')

    def display_flowers(self, obj):
        return ", ".join([flower.name for flower in obj.flowers.all()])
    display_flowers.short_description = 'Flowers'

@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('pk','flower', 'stock_price')