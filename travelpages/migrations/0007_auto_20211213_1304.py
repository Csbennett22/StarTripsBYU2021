# Generated by Django 3.2.8 on 2021-12-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelpages', '0006_auto_20211213_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelplanet',
            name='main_photo',
        ),
        migrations.AddField(
            model_name='customer',
            name='main_photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]