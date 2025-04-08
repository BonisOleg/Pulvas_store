# products.py

from django.shortcuts import render

# Create your views here.
def product_list_view(request):
    """Відображає список товарів.
    Динамічно призначає класи кольорів карткам для кращого візуального розподілу.
    """
    # Тестові дані без жорстко закодованих кольорів
    test_products_data = [
        {'id': 1, 'name': 'Товар 1', 'description': 'Опис товару 1', 'price': 150},
        {'id': 2, 'name': 'Товар 2', 'description': 'Дуже довгий опис товару 2...', 'price': 250},
        {'id': 3, 'name': 'Товар 3', 'description': 'Опис товару 3', 'price': 350},
        {'id': 4, 'name': 'Товар 4', 'description': 'Опис товару 4', 'price': 160},
        {'id': 5, 'name': 'Товар 5', 'description': 'Опис товару 5', 'price': 260},
        {'id': 6, 'name': 'Товар 6', 'description': 'Опис товару 6', 'price': 360},
    ]

    # Список доступних класів кольорів
    color_classes = ['bg-primary', 'bg-accent-2', 'bg-accent-3']
    num_colors = len(color_classes)
    num_columns = 3 # Припускаємо 3 колонки для розрахунку патерну

    # Додаємо клас кольору до кожного продукту
    products_with_color = []
    for i, product_data in enumerate(test_products_data):
        # Розрахунок індексу кольору для зміщення в кожному рядку
        row = i // num_columns
        col = i % num_columns
        color_index = (col + row) % num_colors
        product_data['color_class'] = color_classes[color_index]
        products_with_color.append(product_data)

    context = {
        'products': products_with_color
    }
    return render(request, 'shop/products/product_list.html', context) 