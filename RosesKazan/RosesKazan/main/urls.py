from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page, name='home'),
    path('get_image/<int:flower_id>/', get_flower_image, name='get_flower_image'),
]