from django.db import IntegrityError
from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout



def auth_page(request):
    form = AuthForm()  # Объявляем переменную form заранее

    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            login_username = form.cleaned_data.get('login')  # Переименуйте переменную login
            password = form.cleaned_data.get('password')
            user = authenticate(username=login_username, password=password)  # Используйте новое имя переменной
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Неверный логин или пароль')
    else:
        form = AuthForm()

    return render(request, "auth.html", {'authform': form})


def sign_up_page(request):

    if request.method == 'POST':
        sign_up_form = UserRegistrationForm(request.POST)
        if sign_up_form.is_valid():
            new_user = sign_up_form.save(commit=False)
            new_user.set_password(sign_up_form.cleaned_data['password'])
            try:
                new_user.save()
                return redirect('home')
            except IntegrityError as e:
                sign_up_form.add_error('login', 'Извините, этот логин уже используется. Пожалуйста, выберите другой.')


    else:
        sign_up_form = UserRegistrationForm()

    return render(request, "sign_up.html", {'authform': sign_up_form})

def logout_view(request):
    logout(request)
    return redirect('home')
