# Generated by Django 5.2 on 2025-04-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Чоловіче'), ('female', 'Жіноче'), ('unisex', 'Унісекс'), ('accessory', 'Аксесуари')], default=None, max_length=20, null=True, verbose_name='Стать/Тип'),
        ),
        migrations.AddField(
            model_name='product',
            name='season',
            field=models.CharField(blank=True, choices=[('winter', 'Зима'), ('summer', 'Літо'), ('demi-season', 'Весна/Осінь'), ('accessory', 'Аксесуари')], default=None, max_length=20, null=True, verbose_name='Сезон'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['season'], name='shop_produc_season_70e84c_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['gender'], name='shop_produc_gender_04eeb6_idx'),
        ),
    ]
