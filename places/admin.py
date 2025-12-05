from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Place

@admin.register(Place)
class PlaceAdmin(GISModelAdmin):
    list_display = ("name", "category", "created_at")
    search_fields = ("name", "description")
