from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва категорії")
    slug = models.SlugField(max_length=110, unique=True, verbose_name="Слаг")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категорія")
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Зображення")
    size = models.CharField(max_length=50, blank=True, verbose_name="Розмір") # Можливо, потім зробимо складнішим (SizeVariant?)
    available = models.BooleanField(default=True, verbose_name="В наявності")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['name']
        # Індекси можуть покращити швидкість запитів
        indexes = [
            models.Index(fields=['id', 'available']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name 