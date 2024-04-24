from django.http import HttpResponse, FileResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from main.models import *

from main.forms import SearchForm


def create_bouquet(request):
    flowers = Flower_design.objects.all()


    form = SearchForm()
    return render(request, 'bouquet_designer.html', {'form': form, 'flowers': flowers})

def get_flower_image(request, flower_id):
    flower = get_object_or_404(Flower_design, pk=flower_id)
    image_path = flower.flower_image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


def get_greenery_image(request, greenery_id):
    greenery = get_object_or_404(Greenery_design, pk=greenery_id)
    image_path = greenery.greenery_design_image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


def get_packaging_image(request, packaging_id):
    greenery = get_object_or_404(Packaging, pk=packaging_id)
    image_path = greenery.packaging_design_image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


def get_flowers_obj(request):
    flowers = Flower_design.objects.all()
    # Преобразуйте queryset в список словарей, чтобы его можно было сериализовать в JSON
    flowers_data = list(flowers.values())
    return JsonResponse({'flowers': flowers_data})
