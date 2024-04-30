from django.http import HttpResponse, Http404
from django.shortcuts import render
from main.models import *

from main.forms import SearchForm


def profile_page(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        orders = Orders.objects.filter(profile=profile)
        cart_item_bouquets = []
        orders_with_flowers = []

        for order in orders:
            bouquets = Bouquet.objects.filter(order=order)

            for item in bouquets:
                flowers = item.flowers.all()
                greenery = item.greenery.all()
                total_price = item.total_price
                try:
                    packaging = item.packaging
                except:
                    packaging = None
                bouquet = {
                    'order': item.order,
                    'flowers': flowers,
                    'greenerys': greenery,
                    'packaging': packaging,
                    'total_price': total_price
                }
                cart_item_bouquets.append(bouquet)

            order_flowers = OrderFlower.objects.filter(order=order)
            orders_with_flowers.append({'order': order, 'flowers': order_flowers, 'cart_item_bouquets': cart_item_bouquets})
        has_delivered_order = any(order.status == "Получен" for order in orders)
        has_not_empty_order = any(order.status != "Получен" for order in orders)

        if not has_not_empty_order:
            message_empty = 'Заказов нет, сделайте заказ !'
        else:
            message_empty = ''

        if not has_delivered_order:
            message = 'История покупок пуста'
        else:
            message = ''


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
            return render(request, 'profile.html', {'message': message, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message_hist': message, 'message_empty': message_empty})
        else:
            profile.name=name
            profile.lastname=lastname
            profile.address=address
            profile.save()

    if not profile.name or not profile.lastname or not profile.address:
        message = 'Заполните все поля!'
        if profile.address:
            profile_info = {
                'address': profile.address,
            }
            return render(request, 'profile.html', {'message': message, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message_hist': message, 'message_empty': message_empty,'profile_info': profile_info})
        return render(request, 'profile.html', {'message': message, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message_hist': message, 'message_empty': message_empty})
    else:
        # Поля профиля заполнены, показываем данные профиля
        profile_info = {
            'name': profile.name,
            'lastname': profile.lastname,
            'address': profile.address,
        }
        return render(request, 'profile.html', {'cart_item_bouquets':cart_item_bouquets,'profile_info': profile_info, 'email': request.user.email, 'form': form, 'orders_with_flowers': orders_with_flowers, 'message_hist': message, 'message_empty': message_empty})


