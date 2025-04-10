# admin.py

from django.contrib import admin
from .models import Category, Product, ContactMessage

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'size', 'season', 'gender', 'available', 'updated']
    list_filter = ['available', 'season', 'gender', 'category', 'updated']
    list_editable = ['price', 'size', 'season', 'gender', 'available']
    search_fields = ['name', 'description']

    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'category', 'price', 'size')
        }),
        ('Класифікація', {
            'fields': ('season', 'gender')
        }),
        ('Опис та Зображення', {
            'fields': ('description', 'image')
        }),
        ('Статус', {
            'fields': ('available',)
        }),
    )

    # Можна також використовувати readonly_fields, щоб приховати системні поля
    # readonly_fields = ('created', 'updated') # Якщо потрібно приховати їх зовсім 


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_username', 'telegram_phone', 'created_at', 'is_viewed')
    list_filter = ('is_viewed', 'created_at')
    search_fields = ('name', 'telegram_username', 'telegram_phone', 'message')
    list_editable = ('is_viewed',) # Дозволяємо змінювати статус перегляду прямо у списку
    readonly_fields = ('name', 'telegram_username', 'telegram_phone', 'message', 'created_at') # Робимо поля тільки для читання на сторінці редагування

    # Можна розділити на секції для кращої читабельності
    fieldsets = (
        ('Відправник', {
            'fields': ('name', 'telegram_username', 'telegram_phone')
        }),
        ('Повідомлення', {
            'fields': ('message',)
        }),
        ('Статус', {
            'fields': ('created_at', 'is_viewed')
        }),
    ) 