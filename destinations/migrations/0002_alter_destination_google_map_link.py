# Generated by Django 5.1.2 on 2024-11-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='google_map_link',
            field=models.URLField(max_length=500),
        ),
    ]
