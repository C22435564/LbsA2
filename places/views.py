from rest_framework import viewsets, filters
from rest_framework_gis.filters import DistanceToPointFilter
from .models import Place, Event
from .serializers import PlaceGeoSerializer, EventSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    GeoJSON API for places.

    Supports:
    - Search by name, description, category (?search=...)
    - Distance-based 'near me' queries (?dist=1000&point=-6.26,53.34)
    """
    queryset = Place.objects.all()
    serializer_class = PlaceGeoSerializer

    filter_backends = [filters.SearchFilter, DistanceToPointFilter]
    search_fields = ["name", "description", "category"]

    distance_filter_field = "location"
    distance_filter_convert_meters = True


class EventViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD API for events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
