from django.urls import path
from .views import *

urlpatterns = [
    path('', create_bouquet, name='create_bouquet'),
    path('get_flower_image/<int:flower_id>/', get_flower_image, name='get_flower_image_design'),
    path('get_greenery_image/<int:greenery_id>/', get_greenery_image, name='get_greenery_image_design'),
    path('get_packaging_image/<int:packaging_id>/', get_packaging_image, name='get_packaging_image_design'),
    path('get_flowers/', get_flowers_obj, name='get_flowers_obj')
]