from django.http import HttpResponse, Http404
from django.shortcuts import render
from main.models import *

from main.forms import SearchForm


def profile_page(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        orders = Orders.objects.filter(profile=profile)

        orders_with_flowers = []
        for order in orders:
            order_flowers = OrderFlower.objects.filter(order=order)
            orders_with_flowers.append({'order': order, 'flowers': order_flowers})
        has_delivered_order = any(order.status == "Получен" for order in orders)
        if not has_delivered_order:
            message = 'История покупок пуста'
        else:
            message = ''

        if profile:
            all_cart_items = CartItem.objects.filter(profile=profile)
            cart_item_ids = [item.flower.id for item in all_cart_items]
        else:
            cart_item_ids = []  # Пользователь не имеет профиля или корзины
    else:
        raise Http404("Страница не найдена")

    form = SearchForm(request.GET or None)

    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('last_name')
        address = request.POST.get('address')

        if not name or not lastname or not address:
            # Один или несколько из полей не заполнены
            message = 'Заполните все поля!'
            return render(request, 'profile.html', {'message': message, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message': message})
        else:
            profile.name=name
            profile.lastname=lastname
            profile.address=address
            profile.save()

    if not profile.name or not profile.lastname or not profile.address:
        # Если какое-то из полей не заполнено, показываем сообщение об ошибке
        message = 'Заполните все поля!'
        return render(request, 'profile.html', {'message': message, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message': message})
    else:
        # Поля профиля заполнены, показываем данные профиля
        profile_info = {
            'name': profile.name,
            'lastname': profile.lastname,
            'address': profile.address,
        }
        return render(request, 'profile.html', {'profile_info': profile_info, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message': message})


