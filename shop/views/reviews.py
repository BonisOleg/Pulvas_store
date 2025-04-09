# reviews.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def reviews_view(request: HttpRequest) -> HttpResponse:
    """Відображає сторінку зі списком відгуків (заглушка)."""
    # TODO: Отримати реальні відгуки з бази даних
    test_reviews = [] # Поки порожній список
    context = {
        'reviews': test_reviews
    }
    return render(request, 'shop/reviews/review_list.html', context)

# Функція для додавання відгуку поки не використовується і закоментована в urls.py
# def add_review_view(request: HttpRequest) -> HttpResponse:
#     """Обробляє додавання нового відгуку (заглушка)."""
#     # TODO: Реалізувати логіку форми додавання відгуку (Django Forms)
#     if request.method == 'POST':
#         pass
#     # Рендерити шаблон з формою для GET-запиту
#     pass 

# Create your views here. 