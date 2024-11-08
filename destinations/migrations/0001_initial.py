# Generated by Django 5.1.2 on 2024-10-30 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=50)),
                ('location_state', models.CharField(max_length=50)),
                ('location_district', models.CharField(max_length=50)),
                ('google_map_link', models.URLField()),
                ('image', models.ImageField(upload_to='destination_images/')),
                ('description', models.TextField()),
            ],
        ),
    ]