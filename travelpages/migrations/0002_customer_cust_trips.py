# Generated by Django 3.2.8 on 2021-12-11 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cust_trips',
            field=models.ManyToManyField(blank=True, to='travelpages.Trip'),
        ),
    ]