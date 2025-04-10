from typing import List, Dict, Any, Iterable
from django.db.models.query import QuerySet
from ..models import Product # Імпортуємо Product для перевірки типів та доступу до полів

def _assign_color_classes(products: Iterable[Product], num_columns: int = 3) -> List[Dict[str, Any]]:
    """Допоміжна функція для динамічного призначення класів кольорів карткам.

    Args:
        products: Ітерабельний об'єкт (QuerySet або список) з об'єктами Product.
        num_columns: Очікувана кількість колонок у сітці для розрахунку патерну.

    Returns:
        Список словників, де кожен словник представляє товар 
        з усіма потрібними полями для картки та доданим ключем 'color_class'.
    """
    color_classes = ['bg-primary', 'bg-accent-2', 'bg-accent-3']
    num_colors = len(color_classes)
    products_with_color = []

    # Перетворюємо QuerySet на список, щоб отримати індекс через enumerate
    # або просто використовуємо список, якщо він вже був переданий.
    product_list = list(products)

    for i, product_obj in enumerate(product_list):
        # Створюємо словник з потрібними даними з об'єкта Product
        main_image_obj = product_obj.get_main_image() # Отримуємо головне фото (об'єкт ProductImage або None)
        product_data = {
            'id': product_obj.id,
            'name': product_obj.name,
            'description': product_obj.description,
            'price': product_obj.price,
            # Тепер передаємо сам об'єкт ProductImage (або None), щоб шаблон мав доступ до image.url
            'image_obj': main_image_obj, 
            # Додавай інші поля, якщо вони потрібні в картці
        }
        
        # Розрахунок індексу кольору для зміщення в кожному рядку
        row = i // num_columns
        col = i % num_columns
        color_index = (col + row) % num_colors
        product_data['color_class'] = color_classes[color_index]
        
        products_with_color.append(product_data)
        
    return products_with_color 