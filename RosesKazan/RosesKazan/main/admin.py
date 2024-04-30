from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile','bouquet', 'flower', 'quantity')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'flower', 'discount_price')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'name', 'lastname', 'address')


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'free_flowers', 'flower_image', 'image_preview', 'price')

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
    list_display = ('pk', 'profile', 'order_number', 'status', 'order_date', 'arrival_time', 'price')

    """ def display_flowers(self, obj):
         return ", ".join([flower.name for flower in obj.flowers.all()])

     display_flowers.short_description = 'Flowers'"""


@admin.register(Stocks)
class StocksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'flower', 'stock_price')


@admin.register(OrderFlower)
class OrderFlowerAdmin(admin.ModelAdmin):
    list_display = ('pk','order', 'flower', 'quantity')


@admin.register(Flower_design)
class Flower_designAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image_preview', 'name', 'price', 'quantity')

    def image_preview(self, obj):
        # Отображение изображения в админке
        if obj.flower_image:
            flower_id = obj.pk
            url = reverse('get_flower_image_design', args=[flower_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    image_preview.short_description = 'Image Preview'

@admin.register(Greenery_design)
class Greenery_designAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image_preview', 'name', 'price')

    def image_preview(self, obj):
        # Отображение изображения в админке
        if obj.greenery_design_image:
            greenery_id = obj.pk
            url = reverse('get_greenery_image_design', args=[greenery_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    image_preview.short_description = 'Image Preview'

@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image_preview', 'name', 'price')
    def image_preview(self, obj):
        # Отображение изображения в админке
        if obj.packaging_design_image:
            packaging_id = obj.pk
            url = reverse('get_packaging_image_design', args=[packaging_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    image_preview.short_description = 'Image Preview'

@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ('pk','order', 'display_flowers', 'display_greenery', 'display_packaging', 'total_price')

    def display_flowers(self, obj):
        return ", ".join([flower.name for flower in obj.flowers.all()])

    def display_greenery(self, obj):
        return ", ".join([greenery.name for greenery in obj.greenery.all()])

    def display_packaging(self, obj):
        return obj.packaging.name if obj.packaging else None

    display_flowers.short_description = 'Flowers'
    display_greenery.short_description = 'Greenery'
    display_packaging.short_description = 'Packaging'