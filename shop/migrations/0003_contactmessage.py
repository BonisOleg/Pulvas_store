# Generated by Django 5.2 on 2025-04-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_gender_product_season_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('telegram_username', models.CharField(blank=True, max_length=100, verbose_name='Telegram Username')),
                ('telegram_phone', models.CharField(blank=True, max_length=20, verbose_name='Telegram Phone')),
                ('message', models.TextField(verbose_name='Повідомлення')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата відправки')),
                ('is_viewed', models.BooleanField(default=False, verbose_name='Переглянуто')),
            ],
            options={
                'verbose_name': 'Повідомлення з контактої форми',
                'verbose_name_plural': 'Повідомлення з контактої форми',
                'ordering': ['-created_at'],
            },
        ),
    ]
