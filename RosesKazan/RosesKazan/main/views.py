from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *

def main_page(request):
    flowers = Flowers.objects.all()#["цветок 1", "цветок 2", "цветок 3", "цветок 4", "цветок 5", "цветок 6", "цветок 7", "цветок 8", "цветок 9", "цветок 10", "цветок 11", "цветок 12"]
    roses = ["роза 1", "роза 2", "роза 3", "роза 4", "роза 5", "роза 6", "роза 7", "роза 8", "роза 9", "роза 10", "роза 11", "роза 12"]
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            try:
                result = Flowers.objects.filter(name=form.cleaned_data['query'])
            except:
                result = "Не найдено"
                form = SearchForm()
            return render(request, "results.html", {'form': form,'flowers': result, 'title': 'Главная страница'})
        else:
            form = SearchForm()
    return render(request, "stocks.html", {'form': form, 'title': 'Главная страница', "flowers": flowers, "roses": roses})

def get_flower_image(request, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)
    # Путь к изображению в MEDIA_ROOT
    image_path = flower.flower_image.path
    # Отправляем файл в ответе
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')