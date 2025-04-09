# products.py

from django.shortcuts import render # Видалено get_object_or_404, поки не використовується
from django.http import HttpRequest, HttpResponse
from typing import List, Dict, Any

# Тестові дані (можна винести в окремий файл/сервіс пізніше)
TEST_PRODUCTS_DATA: List[Dict[str, Any]] = [
    {'id': 1, 'name': 'Товар 1', 'description': 'Опис товару 1', 'price': 150},
    {'id': 2, 'name': 'Товар 2', 'description': 'Дуже довгий опис товару 2...', 'price': 250},
    {'id': 3, 'name': 'Товар 3', 'description': 'Опис товару 3', 'price': 350},
    {'id': 4, 'name': 'Товар 4', 'description': 'Опис товару 4', 'price': 160},
    {'id': 5, 'name': 'Товар 5', 'description': 'Опис товару 5', 'price': 260},
    {'id': 6, 'name': 'Товар 6', 'description': 'Опис товару 6', 'price': 360},
]

def _assign_color_classes(products: List[Dict[str, Any]], num_columns: int = 3) -> List[Dict[str, Any]]:
    """Допоміжна функція для динамічного призначення класів кольорів карткам.

    Args:
        products: Список словників з даними товарів.
        num_columns: Очікувана кількість колонок у сітці для розрахунку патерну.

    Returns:
        Список товарів з доданим ключем 'color_class'.
    """
    color_classes = ['bg-primary', 'bg-accent-2', 'bg-accent-3']
    num_colors = len(color_classes)
    products_with_color = []
    for i, product_data in enumerate(products):
        # Розрахунок індексу кольору для зміщення в кожному рядку
        row = i // num_columns
        col = i % num_columns
        color_index = (col + row) % num_colors
        product_data['color_class'] = color_classes[color_index]
        products_with_color.append(product_data)
    return products_with_color

def product_list_view(request: HttpRequest) -> HttpResponse:
    """Відображає головну сторінку зі списком товарів.
    
    Використовує тестові дані та призначає карткам кольори для візуалізації.
    """
    # Копіюємо тестові дані, щоб не змінювати оригінал
    products_data = [p.copy() for p in TEST_PRODUCTS_DATA] 
    products_with_color = _assign_color_classes(products_data)
    
    context = {
        'products': products_with_color
    }
    return render(request, 'shop/products/product_list.html', context)

def product_detail_view(request: HttpRequest, product_id: int) -> HttpResponse:
    """Відображає сторінку з детальною інформацією про товар (заглушка)."""
    # TODO: Замінити на реальне отримання товару з бази даних
    # product = get_object_or_404(Product, pk=product_id) 
    # Наразі використовуємо тестові дані
    product = {
        'id': product_id, 
        'name': f'Товар {product_id}', 
        'description': f'Детальний опис товару {product_id}', 
        'price': 150 + product_id * 10
    }
    context = {
        'product': product
    }
    return render(request, 'shop/products/product_detail.html', context) 