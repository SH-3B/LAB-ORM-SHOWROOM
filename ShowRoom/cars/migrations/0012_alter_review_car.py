# Generated by Django 5.1.3 on 2024-11-24 14:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_reviews', to='cars.car'),
        ),
    ]
