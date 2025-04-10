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
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Зображення")
    size = models.CharField(max_length=50, blank=True, verbose_name="Розмір") # Можливо, потім зробимо складнішим (SizeVariant?)
    # --- Нові поля --- >
    season = models.CharField(
        max_length=20,
        choices=ProductSeason.choices,
        default=None, # Або якийсь дефолт?
        null=True,
        blank=True,
        verbose_name="Сезон"
    )
    gender = models.CharField( # Перейменував з gender_type для стислості
        max_length=20,
        choices=ProductGender.choices,
        default=None,
        null=True,
        blank=True,
        verbose_name="Стать/Тип"
    )
    # < --- Нові поля ---
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
            models.Index(fields=['season']), # Додано індекс
            models.Index(fields=['gender']), # Додано індекс
        ]

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    """Модель для зберігання повідомлень з контактної форми."""
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    # Зберігаємо обидва варіанти, хоча б один має бути заповнений (валідація у view/form)
    telegram_username = models.CharField(max_length=100, blank=True, verbose_name="Telegram Username")
    telegram_phone = models.CharField(max_length=20, blank=True, verbose_name="Telegram Phone")
    message = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")
    is_viewed = models.BooleanField(default=False, verbose_name="Переглянуто") # Для позначки в адмінці

    class Meta:
        verbose_name = "Повідомлення з контактої форми"
        verbose_name_plural = "Повідомлення з контактої форми"
        ordering = ['-created_at'] # Спочатку новіші

    def __str__(self):
        # Показуємо ім'я та початок повідомлення для зручності
        return f"Повідомлення від {self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})" 