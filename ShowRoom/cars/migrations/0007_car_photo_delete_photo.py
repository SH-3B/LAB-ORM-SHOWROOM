# Generated by Django 5.1.3 on 2024-11-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_photo_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cars_photos/'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
