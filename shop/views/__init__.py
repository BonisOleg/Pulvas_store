# shop/views/__init__.py

# Імпортуємо функції view з кожного модуля
from .products import product_list_view, product_detail_view
from .reviews import reviews_view 
from .contact import contact_view
# Модуль availability видалено
from .general import about_us_view
from .catalog import catalog_view
from .availability import availability_view

# Визначаємо, що експортується
__all__ = [
    'product_list_view',
    'product_detail_view',
    'reviews_view',
    'contact_view',
    # Функція check_availability_view видалена
    'about_us_view',
    'catalog_view',
    'availability_view',
]

# Test comment to check if editing works now. 