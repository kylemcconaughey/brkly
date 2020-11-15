from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class Location(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    description = models.TextField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    coordinates = LocationField(
        map_attrs={
            "style": "mapbox://styles/mapbox/streets-v11",
            "center": (35.921637, -79.077887),
            "zoom": 5,
            "rotate": True,
            "navigation_buttons": True,
            "track_location_button": True,
        }
    )  # this gets reversed when delivered with the api for some reason?

    address = AddressAutoHiddenField()

    class LocationTypeChoices(models.TextChoices):
        PARK = "PA", ("Dog Park")
        RESTAURANT = "RE", ("Restaurant")
        VET = "VE", ("Veterinarian")
        TRAIL = "TR", ("Trail")
        HOUSE = "HO", ("House")

    location_type = models.CharField(
        max_length=2,
        choices=LocationTypeChoices.choices,
        default=LocationTypeChoices.PARK,
        null=True,
        blank=True,
    )