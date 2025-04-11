from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Головна сторінка (колишній список товарів)
    path('', views.product_list_view, name='home'),
    # Старий шлях для списку товарів тепер не використовується
    # path('products/', views.product_list_view, name='product_list'), 
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),

    # Каталог товарів (нова сторінка)
    path('catalog/', views.catalog_view, name='catalog'),

    # Відгуки - ВИДАЛЕНО
    # path('reviews/', views.reviews_view, name='reviews'),
    # Маршрут для додавання відгуку поки не активний
    # path('reviews/add/', views.add_review_view, name='add_review'), 

    # Контакти
    path('contact/', views.contact_view, name='contact'),

    # Шлях check-availability видалено
    # path('check-availability/', views.check_availability_view, name='check_availability'),

    # Про нас
    path('about-us/', views.about_us_view, name='about_us'),

    # Додайте інші шляхи тут
    path('availability/', views.availability_view, name='availability'),
] 