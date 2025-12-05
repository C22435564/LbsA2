from rest_framework import viewsets, filters
from rest_framework_gis.filters import DistanceToPointFilter
from .models import Place
from .serializers import PlaceGeoSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all().order_by("-created_at")
    serializer_class = PlaceGeoSerializer
    filter_backends = [filters.SearchFilter, DistanceToPointFilter]
    search_fields = ["name", "description", "category"]

    # DistanceToPointFilter: allows /api/places/?dist=5000&point=-6.26,53.34
    distance_filter_field = "location"
    distance_filter_convert_meters = True
