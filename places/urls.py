from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet, EventViewSet

router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")
router.register(r"events", EventViewSet, basename="event")

urlpatterns = router.urls
