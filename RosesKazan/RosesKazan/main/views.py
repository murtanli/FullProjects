from django.contrib import messages
from django.db.models import Q
from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *


def main_page(request):
    flowers = Flowers.objects.all()
    roses = Flowers.objects.filter(category="Розы")
    chrysanthemums = Flowers.objects.filter(category="Хризантемы")
    low_price = Flowers.objects.filter(price__lt=2500)

    discounts = Discount.objects.all()
    disc_flowers = [discount.flower for discount in discounts]

    cart_item_ids = []

    if request.user.is_authenticated:
        all_cart_items = CartItem.objects.filter(user=request.user)
        cart_item_ids = [item.flower.id for item in all_cart_items]

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query_lower = form.cleaned_data['query'].lower()
            try:
                result = Flowers.objects.filter(Q(name__icontains=query_lower[:-2]))
                if not result.exists():
                    result = Flowers.objects.filter(Q(category__icontains=query_lower[:-2]))
            except:
                result = "Не найдено"
                form = SearchForm()
            return render(request, "results.html", {"all_cart_items": cart_item_ids, 'form': form,'flowers': result, 'title': 'Главная страница'})
        else:
            form = SearchForm()

    return render(request, "stocks.html", {
        'form': form,
        'title': 'Главная страница',
        "flowers": flowers,
        "roses": roses,
        "chrysanthemums": chrysanthemums,
        "discounts": discounts,
        "low_price": low_price,
        "all_cart_items": cart_item_ids
    })

def get_flower_image(request, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)
    image_path = flower.flower_image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


def add_to_cart(request):
    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower = get_object_or_404(Flowers, id=flower_id)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, flower=flower)

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('home')
    else:
        return redirect('home')

def del_added_cart(request):
    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower = get_object_or_404(Flowers, id=flower_id)
        try:
            cart_item = CartItem.objects.get(user=request.user, flower=flower)
        except CartItem.DoesNotExist:
            return redirect('log_in_page')
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return redirect('home')
    else:
        return redirect('home')

def del_flower(request):
    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower = get_object_or_404(Flowers, id=flower_id)
        try:
            cart_item = CartItem.objects.get(user=request.user, flower=flower)
        except CartItem.DoesNotExist:
            return redirect('log_in_page')
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        return redirect('cart_page')
    else:
        return redirect('cart_page')

def cart_page(request):
    if request.user.is_authenticated:
        all_cart_items = CartItem.objects.filter(user=request.user)
        cart_item_ids = [item.flower.id for item in all_cart_items]
    else:
        raise Http404("Страница не найдена")

    discounts = Discount.objects.all()
    disc_flowers = [discount.flower.id for discount in discounts]

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query_lower = form.cleaned_data['query'].lower()
            try:
                result = Flowers.objects.filter(Q(name__icontains=query_lower[:-2]))
                if not result.exists():
                    result = Flowers.objects.filter(Q(category__icontains=query_lower[:-2]))
            except:
                result = "Не найдено"
                form = SearchForm()
            return render(request, "results.html", {"all_cart_items": cart_item_ids, 'form': form,'flowers': result, 'title': 'Главная страница'})
        else:
            form = SearchForm()
    return render(request, "cart_page.html", {
        'form': form,
        'cart_items': all_cart_items,
        'discounts': discounts,
        'disc_flowers_id': disc_flowers,
    })




