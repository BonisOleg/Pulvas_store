from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..models import Product, ProductSeason, ProductGender
from ..utils.card_utils import _assign_color_classes

def availability_view(request: HttpRequest) -> HttpResponse:
    """Відображає сторінку з товарами, що є в наявності, з можливістю фільтрації."""
    # Базовий запит: тільки доступні товари
    products_query = Product.objects.filter(available=True)

    # Отримуємо параметри фільтрації з GET-запиту
    selected_season = request.GET.get('season')
    selected_gender = request.GET.get('gender')
    selected_price_min = request.GET.get('price_min')
    selected_price_max = request.GET.get('price_max')

    # Застосовуємо фільтри, якщо вони вибрані
    if selected_season and selected_season in ProductSeason.values:
        products_query = products_query.filter(season=selected_season)
    if selected_gender and selected_gender in ProductGender.values:
        products_query = products_query.filter(gender=selected_gender)

    # Фільтр за ціною "від"
    if selected_price_min:
        try:
            price_min = int(selected_price_min)
            if price_min >= 0:
                products_query = products_query.filter(price__gte=price_min)
        except (ValueError, TypeError):
            pass # Ігноруємо некоректне значення ціни

    # Фільтр за ціною "до"
    if selected_price_max:
        try:
            price_max = int(selected_price_max)
            if price_max >= 0:
                products_query = products_query.filter(price__lte=price_max)
        except (ValueError, TypeError):
            pass # Ігноруємо некоректне значення ціни

    # ЗАСТОСОВУЄМО КОЛЬОРИ ДО КАРТОК
    # Спочатку перетворюємо QuerySet на список словників і додаємо класи кольорів
    # TODO: Перевірити, чи _assign_color_classes коректно обробляє QuerySet і повертає потрібні поля
    products_with_color = _assign_color_classes(list(products_query))
    # КІНЕЦЬ ЗАСТОСУВАННЯ КОЛЬОРІВ

    # Отримуємо всі можливі значення для фільтрів (для відображення в UI)
    # Використовуємо .values_list().distinct() для ефективності
    available_seasons = Product.objects.filter(available=True).values_list('season', flat=True).distinct()
    available_genders = Product.objects.filter(available=True).values_list('gender', flat=True).distinct()

    # Створюємо словники для зручного відображення міток у шаблоні
    season_choices = {choice.value: choice.label for choice in ProductSeason}
    gender_choices = {choice.value: choice.label for choice in ProductGender}

    context = {
        'products': products_with_color, # Тепер передаємо список словників з кольорами!
        'seasons': [(s, season_choices.get(s)) for s in available_seasons if s], # Список доступних сезонів (значення, мітка)
        'genders': [(g, gender_choices.get(g)) for g in available_genders if g], # Список доступних статей (значення, мітка)
        'selected_season': selected_season,
        'selected_gender': selected_gender,
        'selected_price_min': selected_price_min,
        'selected_price_max': selected_price_max,
        'season_choices': season_choices, # Для відображення назви активного фільтру
        'gender_choices': gender_choices, # Для відображення назви активного фільтру
    }
    return render(request, 'shop/availability/availability.html', context)