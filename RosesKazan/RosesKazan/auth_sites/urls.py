from django.urls import path
from .views import *


urlpatterns = [
    path('login/', auth_page, name="log_in_page"),
    path('sign_up/', sign_up_page, name="sign_up_page"),
    path('logout/', logout_view, name="logout_view")
]