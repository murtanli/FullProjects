from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page, name='home'),
    path('get_image/<int:flower_id>/', get_flower_image, name='get_flower_image'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('del_to_cart/', del_added_cart, name='del_to_cart'),
    path('cart/', cart_page, name='cart_page'),
]