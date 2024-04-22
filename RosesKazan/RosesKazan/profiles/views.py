from django.http import HttpResponse
from django.shortcuts import render
from main.models import *


def profile_page(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if not profile.name or not profile.lastname:
        message = f'Заполните поля !'
        return render(request, 'profile.html', {'message': message,'email': user.email})
    else:
        profile_info = {

        }
    return render(request, 'profile.html')