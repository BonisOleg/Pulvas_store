# contact.py

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def contact_view(request: HttpRequest) -> HttpResponse:
    """Відображає сторінку контактів та обробляє відправку форми (заглушка)."""
    
    if request.method == 'POST':
        # TODO: Реалізувати обробку POST-запиту: 
        # - валідація даних форми (використовувати Django Forms)
        # - відправка повідомлення (наприклад, на email або в Telegram)
        # - показ повідомлення про успіх/помилку
        print("Form submitted:", request.POST) # Тимчасовий вивід даних
        # Можна додати повідомлення для користувача через messages framework
        # messages.success(request, 'Ваше повідомлення успішно надіслано!')
        # return redirect('shop:contact') # Перенаправлення після успішної відправки
        pass # Поки що нічого не робимо з POST

    # Для GET-запиту просто відображаємо порожню форму
    return render(request, 'shop/contact/contact_form.html')

# Create your views here. 