from typing import List, Dict, Any

def _assign_color_classes(products: List[Dict[str, Any]], num_columns: int = 3) -> List[Dict[str, Any]]:
    """Допоміжна функція для динамічного призначення класів кольорів карткам.

    Args:
        products: Список словників або об'єктів з даними товарів.
                  Якщо це QuerySet, він буде перетворений на список словників.
        num_columns: Очікувана кількість колонок у сітці для розрахунку патерну.

    Returns:
        Список товарів (словників) з доданим ключем 'color_class'.
    """
    color_classes = ['bg-primary', 'bg-accent-2', 'bg-accent-3']
    num_colors = len(color_classes)
    products_with_color = []
    
    # Перевіряємо, чи це QuerySet і конвертуємо, якщо так (потрібно для .values())
    # Або чи це список об'єктів, з яких треба зробити словники
    # Або чи це вже список словників
    product_list = []
    if hasattr(products, 'values'): # Схоже на QuerySet
        # TODO: Визначити, які поля потрібні з моделі Product
        # Поки що візьмемо основні для картки + ті, що вже є в тестових даних
        try:
            product_list = list(products.values('id', 'name', 'description', 'price', 'image')) # Додаємо image
        except AttributeError: # Можливо, це не QuerySet, а щось інше
             product_list = list(products) # Спробуємо просто як список
    elif products and isinstance(products[0], object) and not isinstance(products[0], dict):
        # Список об'єктів, перетворюємо на словники
        # TODO: Знову ж, визначити потрібні поля
        product_list = [
            {
                'id': p.id,
                'name': p.name,
                'description': p.description,
                'price': p.price,
                'image': p.image # Додаємо image
             } for p in products
        ]
    else:
        # Вважаємо, що це вже список словників
        product_list = products

    for i, product_data in enumerate(product_list):
        # Розрахунок індексу кольору для зміщення в кожному рядку
        row = i // num_columns
        col = i % num_columns
        color_index = (col + row) % num_colors
        product_data['color_class'] = color_classes[color_index]
        products_with_color.append(product_data)
        
    return products_with_color 