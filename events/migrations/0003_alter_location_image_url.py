# Generated by Django 4.0.3 on 2023-09-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_location_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
