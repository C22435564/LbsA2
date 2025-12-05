from django.contrib.gis.db import models


class Place(models.Model):
    CATEGORY_PUB = "pub"
    CATEGORY_CAFE = "cafe"
    CATEGORY_PARK = "park"
    CATEGORY_OTHER = "other"

    CATEGORY_CHOICES = [
        (CATEGORY_PUB, "Pub"),
        (CATEGORY_CAFE, "Café"),
        (CATEGORY_PARK, "Park"),
        (CATEGORY_OTHER, "Other"),
    ]

    name = models.CharField(max_length=200, help_text="Name of the place.")
    description = models.TextField(blank=True, help_text="Short description.")
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_OTHER,
        help_text="Type of place."
    )
    location = models.PointField(
        geography=True,
        help_text="Geographic location (WGS84 lat/lon)."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["category"]),
        ]

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    place = models.ForeignKey(
        Place,
        related_name="events",
        on_delete=models.CASCADE,
        help_text="Place where the event takes place.",
    )
    title = models.CharField(max_length=200)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["starts_at"]

    def __str__(self) -> str:
        return f"{self.title} @ {self.place.name}"
