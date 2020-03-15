# Generated by Django 3.0.3 on 2020-03-15 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_product_base_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pictures',
        ),
        migrations.AddField(
            model_name='product',
            name='base_view',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Product  Image'),
        ),
        migrations.AddField(
            model_name='productpicture',
            name='productId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product ID'),
        ),
    ]
