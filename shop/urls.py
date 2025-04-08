from django.urls import path
from .views import products  # Імпортуємо модуль views.products

app_name = 'shop'

urlpatterns = [
    path('', products.product_list_view, name='home'),
    path('products/', products.product_list_view, name='product_list'),
    # Додайте інші шляхи тут
] 