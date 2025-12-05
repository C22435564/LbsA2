from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Place, Event


@admin.register(Place)
class PlaceAdmin(GISModelAdmin):
    list_display = ("name", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "place", "starts_at")
    list_filter = ("place", "starts_at")
    search_fields = ("title", "description")
