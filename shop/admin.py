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
    list_display = ['name', 'category', 'price', 'size', 'available', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available'] # Дозволяємо редагувати ціну та наявність прямо зі списку
    search_fields = ['name', 'description']
    prepopulated_fields = {'description': ('name',)} # Приклад: можна прибрати, якщо не треба автозаповнення опису 