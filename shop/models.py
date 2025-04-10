from django.db import models
from django.core.exceptions import ValidationError # Додаємо для валідації

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

# --- Константи для вибору --- >
class ProductSeason(models.TextChoices):
    WINTER = 'winter', 'Зима'
    SUMMER = 'summer', 'Літо'
    DEMI = 'demi-season', 'Весна/Осінь'
    ACCESSORY = 'accessory', 'Аксесуари' # Додано для аксесуарів

class ProductGender(models.TextChoices):
    MALE = 'male', 'Чоловіче'
    FEMALE = 'female', 'Жіноче'
    UNISEX = 'unisex', 'Унісекс'
    ACCESSORY = 'accessory', 'Аксесуари' # Співпадає з сезоном
# < --- Константи для вибору ---

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категорія")
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    size = models.CharField(max_length=50, blank=True, verbose_name="Розмір")
    season = models.CharField(
        max_length=20,
        choices=ProductSeason.choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Сезон"
    )
    gender = models.CharField(
        max_length=20,
        choices=ProductGender.choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Стать/Тип"
    )
    available = models.BooleanField(default=True, verbose_name="В наявності")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'available']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
            models.Index(fields=['season']),
            models.Index(fields=['gender']),
        ]

    def __str__(self):
        return self.name

    # Додаємо метод для отримання головного зображення
    def get_main_image(self):
        # related_name='images' буде визначено в ProductImage
        main_image = self.images.filter(is_main=True).first()
        if main_image:
            return main_image
        # Якщо головне не позначено, повертаємо перше знайдене або None
        return self.images.first()

    def get_main_image_url(self):
        main_image = self.get_main_image()
        if main_image and main_image.image:
            return main_image.image.url
        return None # Або URL до плейсхолдера

# --- НОВА МОДЕЛЬ ДЛЯ ЗОБРАЖЕНЬ ТОВАРУ --- >
def product_image_upload_path(instance, filename):
    # Функція для генерації шляху: media/products/<product_id>/<filename>
    return f'products/{instance.product.id}/{filename}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField(upload_to=product_image_upload_path, verbose_name="Зображення")
    is_main = models.BooleanField(default=False, verbose_name="Головне фото", help_text="Позначте одне фото як головне для картки товару")
    # Опціонально: поле для сортування
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Порядок")

    class Meta:
        verbose_name = "Фото товару"
        verbose_name_plural = "Фото товарів"
        ordering = ['order'] # Сортуємо за полем order

    def __str__(self):
        return f"Фото для {self.product.name} ({self.id})"
        
    def save(self, *args, **kwargs):
        # Перед збереженням переконуємось, що лише одне фото є головним
        if self.is_main:
            # Скидаємо is_main для всіх інших фото цього ж товару
            ProductImage.objects.filter(product=self.product).exclude(pk=self.pk).update(is_main=False)
        elif not ProductImage.objects.filter(product=self.product, is_main=True).exclude(pk=self.pk).exists():
             # Якщо це НЕ головне і більше немає головних (крім себе), 
             # а також це перше зображення для товару, робимо його головним автоматично
             # (можна прибрати, якщо не потрібно)
             if not self.pk and not ProductImage.objects.filter(product=self.product).exists():
                 self.is_main = True
            
        super().save(*args, **kwargs)

# < --- КІНЕЦЬ НОВОЇ МОДЕЛІ --- 

class ContactMessage(models.Model):
    """Модель для зберігання повідомлень з контактної форми."""
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    telegram_username = models.CharField(max_length=100, blank=True, verbose_name="Telegram Username")
    telegram_phone = models.CharField(max_length=20, blank=True, verbose_name="Telegram Phone")
    message = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")
    is_viewed = models.BooleanField(default=False, verbose_name="Переглянуто")

    class Meta:
        verbose_name = "Повідомлення з контактої форми"
        verbose_name_plural = "Повідомлення з контактої форми"
        ordering = ['-created_at']

    def __str__(self):
        return f"Повідомлення від {self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})" 