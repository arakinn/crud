# Generated by Django 5.1.3 on 2024-12-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0008_alter_reservation_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='お電話番号'),
        ),
    ]
