from django.contrib import admin
from .models import Race, RaceResult

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ("name", "circuit", "year", "round", "date")
    search_fields = ("name", "circuit")
    list_filter = ("year",)

@admin.register(RaceResult)
class RaceResultAdmin(admin.ModelAdmin):
    list_display = ("race", "driver", "position", "points", "fastest_lap_time")
    list_filter = ("race", "driver", "position")
    search_fields = ("race__name", "driver__first_name", "driver__last_name", "driver__code")
