from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Place

class PlaceGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Place
        geo_field = "location"  # field that holds geometry
        fields = ("id", "name", "description", "category", "created_at", "location")
