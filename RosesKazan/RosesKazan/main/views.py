import json
from datetime import timedelta

from django.contrib import messages
from django.db.models import Q
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import *
from .models import *
import uuid
import json
from django.http import JsonResponse

def main_page(request):
    flowers = Flowers.objects.all()
    roses = Flowers.objects.filter(category="Розы")
    chrysanthemums = Flowers.objects.filter(category="Хризантемы")
    low_price = Flowers.objects.filter(price__lt=2500)

    discounts = Discount.objects.all()
    disc_flowers = [discount.flower for discount in discounts]

    cart_item_ids = []
    cart_item_bouquets = []
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()  # Получить первый профиль или None
        if profile:
            all_cart_items = CartItem.objects.filter(profile=profile)
            for item in all_cart_items:
                try:
                    cart_item_ids.append(item.flower.id)
                except:
                    cart_item_bouquets.append(item.bouquet.id)
            # cart_item_ids = [item.flower.id for item in all_cart_items]
        else:
            cart_item_ids = []  # Пользователь не имеет профиля или корзины
    else:
        cart_item_ids = []  # Пользователь не аутентифицирован

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
            return render(request, "results.html", {"all_cart_items": cart_item_ids,"discounts": discounts,"disc_flowers": disc_flowers, 'form': form,'flowers': result, 'title': 'Главная страница'})
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
        "all_cart_items": cart_item_ids,
        "disc_flowers": disc_flowers
    })

def get_flower_image(request, flower_id):
    flower = get_object_or_404(Flowers, pk=flower_id)
    image_path = flower.flower_image.path
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


def add_to_cart(request):
    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower = get_object_or_404(Flowers, id=flower_id)
        profile = Profile.objects.filter(user=request.user).first()
        cart_item, created = CartItem.objects.get_or_create(profile=profile, flower=flower)

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
            profile = Profile.objects.filter(user=request.user).first()
            cart_item = CartItem.objects.get(profile=profile, flower=flower)
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
            profile = Profile.objects.filter(user=request.user).first()
            cart_item = CartItem.objects.get(profile=profile, flower=flower)
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
    cart_item_ids = []
    cart_item_bouquets = []
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()  # Получить первый профиль или None
        if profile:
            # all_cart_items = CartItem.objects.filter(profile=profile)
            # cart_item_ids = [item.flower.id for item in all_cart_items]
            all_cart_items = CartItem.objects.filter(profile=profile)
            for item in all_cart_items:
                if item.flower != None:
                    cart_item_ids.append(item)
                else:
                    bouquet = Bouquet.objects.get(id=item.bouquet.id)
                    flowers = bouquet.flowers.all()
                    greenery = bouquet.greenery.all()
                    try:
                        packaging = bouquet.packaging
                    except:
                        packaging = None
                    total_price = bouquet.total_price

                    cart_bouquet = {
                        'flowers': flowers,
                        'greenerys': greenery,
                        'packaging': packaging,
                        'total_price': total_price
                    }
                    cart_item_bouquets.append(cart_bouquet)
        else:
            cart_item_ids = []  # Пользователь не имеет профиля или корзины
    else:
        cart_item_ids = []  # Пользователь не аутентифицирован
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
        'cart_items': cart_item_ids,
        'discounts': discounts,
        'disc_flowers_id': disc_flowers,
        'bouquets': cart_item_bouquets,
    })

def place_order(request):
    if request.method == 'POST':
        profile = Profile.objects.filter(user=request.user).first()

        mas_flow = []

        total_price = 0

        if profile and profile.address is None:
            return redirect('add_address')
        else:
            num = 0

            for key, value in request.POST.items():
                if key.startswith('flower_'):
                    num += 1
                    quantity = value

                    if num == 1:
                        flower = Flowers.objects.filter(id = quantity).first()
                        profile = Profile.objects.filter(user=request.user).first()
                        cart = CartItem.objects.get(flower=flower, profile=profile)

                        mas_flow.append(quantity)

                        if Discount.objects.filter(flower=flower):
                            disc_flower = Discount.objects.get(flower=flower)
                            #total_price += int(disc_flower.discount_price)
                        """else:
                            total_price += flower.price"""

                    elif num == 2:
                        mas_flow.append(quantity)
                        num = 0
                        cart.quantity = quantity
                        cart.save()

            for i in range(len(mas_flow)):
                if i % 2 == 0:
                    flower = Flowers.objects.get(id=mas_flow[i ])
                    if Discount.objects.filter(flower=flower):
                        disc_flower = Discount.objects.get(flower=flower)
                        price = int(disc_flower.discount_price) * int(mas_flow[i + 1])
                    else:
                        price = int(flower.price) * int(mas_flow[i + 1])
                    total_price += price

            unique_order_number = False
            while not unique_order_number:
                order_number = str(uuid.uuid4())[:8]

                if not Orders.objects.filter(order_number=order_number).exists():
                    unique_order_number = True

            us_cart = CartItem.objects.filter(profile=profile)

            for item in us_cart:
                if item.bouquet is not None:
                    bouquet = item.bouquet
                    flowers = bouquet.flowers.all()
                    greenery = bouquet.greenery.all()
                    packaging = bouquet.packaging
                    for flower in flowers:
                        total_price += flower.price
                    if greenery is not None:
                        for greenery in greenery:
                            total_price += greenery.price
                    if packaging is not None:
                        total_price += packaging.price

            time_now = timezone.now()
            arrival_date = time_now + timedelta(minutes=60)
            order = Orders.objects.create(
                profile=profile,
                order_number=order_number,
                status="В сборке",
                order_date=time_now,
                arrival_time=arrival_date,
                price=total_price,
                address=profile.address
            )





            for item in us_cart:
                if item.bouquet is not None:
                    bouquet_cart = item.bouquet
                    bouquet_cart.order = order
                    bouquet_cart.save()
                item.delete()

            order.save()

            num = 0
            for i in range(len(mas_flow)):
                num += 1
                if num == 2:
                    order_flow = OrderFlower.objects.create(
                        order=order,
                        flower=Flowers.objects.get(id=mas_flow[i-1]),
                        quantity=int(mas_flow[i])
                    )
                    num = 0
        return redirect('home')
    else:
        # В случае, если метод запроса не POST, вернуть ответ с кодом 405 (Метод не разрешен)
        return HttpResponse(status=405)

def save_cart(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        if address[:6] != 'Казань':
            error_message = 'Доставка доступна только в Казани.'
            return render(request, 'add_address.html', {'error_message': error_message})
        else:
            profile = Profile.objects.filter(user=request.user).first()
            profile.address = address
            profile.save()

            return redirect('cart_page')
    else:
        return redirect('home')


def add_address(request):
    return render(request, 'add_address.html')


