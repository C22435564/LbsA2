from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from places.views import PlaceViewSet
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r"places", PlaceViewSet, basename="place")

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),  # ✅ home
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
