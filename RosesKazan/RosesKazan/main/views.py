from django.shortcuts import render
from .forms import *


def main_page(request):
    flowers = ["цветок 1", "цветок 2", "цветок 3", "цветок 4", "цветок 5", "цветок 6", "цветок 7", "цветок 8", "цветок 9", "цветок 10", "цветок 11", "цветок 12"]
    roses = ["роза 1", "роза 2", "роза 3", "роза 4", "роза 5", "роза 6", "роза 7", "роза 8", "роза 9", "роза 10", "роза 11", "роза 12"]
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            return render(request, "stocks.html", {'result': query, 'title': 'Главная страница'})
        else:
            form = SearchForm()
    return render(request, "stocks.html", {'form': form, 'title': 'Главная страница', "flowers": flowers, "roses": roses})
