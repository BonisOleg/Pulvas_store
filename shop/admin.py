# admin.py

from django.contrib import admin
from .models import Category, Product, ContactMessage, ProductImage

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

# Створюємо інлайн для фотографій
class ProductImageInline(admin.TabularInline): # Або admin.StackedInline для іншого вигляду
    model = ProductImage
    extra = 1 # Кількість порожніх форм для додавання нових фото
    fields = ('image', 'is_main', 'order') # Поля для відображення
    # readonly_fields = ('thumbnail',) # Можна додати показ мініатюри

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'size', 'season', 'gender', 'available', 'updated']
    list_filter = ['available', 'season', 'gender', 'category', 'updated']
    list_editable = ['price', 'size', 'season', 'gender', 'available']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline] # Додаємо інлайн фотографій сюди

    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'category', 'price', 'size')
        }),
        ('Класифікація', {
            'fields': ('season', 'gender')
        }),
        ('Опис', { # Замінено "Опис та Зображення"
            'fields': ('description',)
        }),
        ('Статус', {
            'fields': ('available',)
        }),
    )
    # Поле image тепер не потрібне у fieldsets

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