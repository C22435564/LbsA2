from django.contrib.gis.db import models

class Place(models.Model):
    CATEGORY_CHOICES = [
        ("cafe", "Café"),
        ("park", "Park"),
        ("pub", "Pub"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    location = models.PointField(geography=True)  # GeoDjango field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
