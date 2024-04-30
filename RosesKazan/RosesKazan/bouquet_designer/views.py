import json

from django.http import HttpResponse, FileResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from main.models import *

from main.forms import SearchForm


def create_bouquet(request):
    flowers = Flower_design.objects.all()
    greenerys = Greenery_design.objects.all()
    packaging = Packaging.objects.all()
    form = SearchForm()
    return render(request, 'bouquet_designer.html', {'form': form, 'flowers': flowers,'packaging': packaging, 'greenerys': greenerys})

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

def save_created_bouquet(request):

    if request.method == 'POST':
        selectedFlowerIds = request.POST.get('selectedFlowerIds')
        selectedGreenery = request.POST.get('selectedGreenery')
        selectedPackage = request.POST.get('selectedPackage')
        # print(f'{selectedFlowerIds} \n {selectedGreenery} \n {selectedPackage}')
        try:
            selectedGreenery = json.loads(selectedGreenery)
        except:
            selectedGreenery = None

        try:
            selectedPackage = json.loads(selectedPackage)
        except:
            selectedPackage = None

        bouquet = Bouquet.objects.create(total_price=0)
        total_price = 0
        profile = Profile.objects.get(user=request.user)

        selectedFlowerIds = json.loads(selectedFlowerIds)
        for item in selectedFlowerIds:
            item = int(item)
            flower = Flower_design.objects.get(id=item)
            bouquet.flowers.add(flower)
            total_price += flower.price

        if selectedGreenery != None:
            for item in selectedGreenery:
                item = int(item)
                greenery = Greenery_design.objects.get(id=item)
                bouquet.greenery.add(greenery)
                total_price += greenery.price

        if selectedPackage != None:
            for item in selectedPackage:
                package = Packaging.objects.get(id=int(item))
                bouquet.packaging = package  # Переопределяем поле packaging у букета
                total_price += package.price

        bouquet.total_price = total_price
        bouquet.save()

        sv_cart = CartItem.objects.create(
            profile=profile,
            bouquet=bouquet,
            quantity=1
        )


        return redirect('home')
    else:
        raise Http404("Страница не найдена")