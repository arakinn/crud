# Generated by Django 5.1.3 on 2024-12-12 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_reservationitem_reservation_menu_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='reservationitem',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='reservations.reservation'),
        ),
    ]
