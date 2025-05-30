# Generated by Django 5.2 on 2025-04-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_product_image_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='clicks',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False, verbose_name='Кількість переглядів'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-clicks', '-id'], name='shop_produc_clicks_fdf335_idx'),
        ),
    ]
