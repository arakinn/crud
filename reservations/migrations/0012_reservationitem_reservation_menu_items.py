# Generated by Django 5.1.3 on 2024-12-12 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0011_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.items')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='menu_items',
            field=models.ManyToManyField(through='reservations.ReservationItem', to='reservations.items', verbose_name='注文メニュー'),
        ),
    ]
