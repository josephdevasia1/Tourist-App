from django.db import models

class Destination(models.Model):
    place_name = models.CharField(max_length=100)
    weather = models.CharField(max_length=50)
    location_state = models.CharField(max_length=50)
    location_district = models.CharField(max_length=50)
    google_map_link = models.URLField(max_length=500)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.place_name
