# contact.py

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from ..models import ContactMessage
from django.contrib import messages

def contact_view(request: HttpRequest) -> HttpResponse:
    """Відображає сторінку контактів та обробляє відправку форми."""
    
    if request.method == 'POST':
        name = request.POST.get('name')
        telegram_username = request.POST.get('telegram_username', '').strip()
        telegram_phone = request.POST.get('telegram_phone', '').strip()
        message_text = request.POST.get('message')

        # Проста валідація: Ім'я та повідомлення обов'язкові,
        # Також хоча б один з контактів Telegram має бути заповнений (і не лише префікс)
        if name and message_text and ( (telegram_username and telegram_username != '@') or (telegram_phone and telegram_phone != '+380') ):
            ContactMessage.objects.create(
                name=name,
                telegram_username=telegram_username if telegram_username != '@' else '', # Зберігаємо порожнім, якщо тільки префікс
                telegram_phone=telegram_phone if telegram_phone != '+380' else '', # Зберігаємо порожнім, якщо тільки префікс
                message=message_text
            )
            messages.success(request, 'Дякуємо! Ваше повідомлення успішно надіслано.')
            return redirect('shop:contact') # Перенаправляємо на цю ж сторінку
        else:
            # Якщо валідація не пройшла
            messages.error(request, 'Будь ласка, заповніть усі обов\'язкові поля та вкажіть хоча б один контакт Telegram.')
            # Залишаємо користувача на сторінці, щоб він міг виправити помилки
            # Можна було б передати введені дані назад у шаблон, але поки що спростимо

    # Для GET-запиту або якщо POST не валідний (і ми не робимо redirect)
    return render(request, 'shop/contact/contact_form.html')

# Create your views here. 