# Generated by Django 5.1.3 on 2024-11-14 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='img',
        ),
    ]
