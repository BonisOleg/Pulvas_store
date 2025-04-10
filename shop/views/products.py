# products.py

from django.shortcuts import render, get_object_or_404 # Додано get_object_or_404
from django.http import HttpRequest, HttpResponse
from typing import List, Dict, Any
from ..utils.card_utils import _assign_color_classes # Додано імпорт
from ..models import Product, ProductImage # Додаємо ProductImage

# Тестові дані більше не використовуються
# TEST_PRODUCTS_DATA: List[Dict[str, Any]] = [...]

# Функцію _assign_color_classes перенесено до shop/utils/card_utils.py
# def _assign_color_classes(products: List[Dict[str, Any]], num_columns: int = 3) -> List[Dict[str, Any]]:
#     """Допоміжна функція для динамічного призначення класів кольорів карткам.
# 
#     Args:
#         products: Список словників з даними товарів.
#         num_columns: Очікувана кількість колонок у сітці для розрахунку патерну.
# 
#     Returns:
#         Список товарів з доданим ключем 'color_class'.
#     """
#     color_classes = ['bg-primary', 'bg-accent-2', 'bg-accent-3']
#     num_colors = len(color_classes)
#     products_with_color = []
#     for i, product_data in enumerate(products):
#         # Розрахунок індексу кольору для зміщення в кожному рядку
#         row = i // num_columns
#         col = i % num_columns
#         color_index = (col + row) % num_colors
#         product_data['color_class'] = color_classes[color_index]
#         products_with_color.append(product_data)
#     return products_with_color

def product_list_view(request: HttpRequest) -> HttpResponse:
    """Відображає головну сторінку зі списком товарів.
    
    Отримує реальні товари з бази даних та призначає карткам кольори.
    """
    # Отримуємо доступні товари з бази даних, сортуємо за датою створення (новіші спочатку)
    all_available_products = Product.objects.filter(available=True).order_by('-created')
    
    # Призначаємо кольори карткам
    products_with_color = _assign_color_classes(all_available_products) # Передаємо QuerySet
    
    context = {
        'products': products_with_color
    }
    return render(request, 'shop/products/product_list.html', context)

def product_detail_view(request: HttpRequest, product_id: int) -> HttpResponse:
    """Відображає сторінку з детальною інформацією про товар та галереєю фото."""
    product = get_object_or_404(Product, pk=product_id)
    # Отримуємо всі зображення для цього товару, відсортовані за полем order
    # .select_related('product') тут не потрібен, бо ми вже маємо product
    product_images = product.images.all() # Використовуємо related_name='images'
    
    context = {
        'product': product,
        'product_images': product_images # Додаємо список зображень у контекст
    }
    return render(request, 'shop/products/product_detail.html', context) 