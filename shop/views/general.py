from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def about_us_view(request: HttpRequest) -> HttpResponse:
    """Відображає статичну сторінку 'Про нас'."""
    return render(request, 'shop/about_us.html') 