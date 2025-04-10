from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ..models import Product

def availability_view(request: HttpRequest) -> HttpResponse:
    """Відображає сторінку з товарами, що є в наявності."""
    # Отримуємо тільки ті товари, де available=True
    available_products = Product.objects.filter(available=True)

    context = {
        'products': available_products,
    }
    return render(request, 'shop/availability/availability.html', context) 