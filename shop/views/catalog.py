from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def catalog_view(request: HttpRequest) -> HttpResponse:
    """Відображає головну сторінку каталогу (наразі з вибором категорій)."""
    
    # TODO: Коли буде реалізовано перехід до конкретних категорій,
    # можливо, ця view буде показувати всі товари або фільтри.
    
    # Наразі просто рендеримо шаблон з папками категорій
    context = {}
    return render(request, 'shop/catalog/catalog.html', context) 