# admin.py

from django.contrib import admin
from .models import Category, Product

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