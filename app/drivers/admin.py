from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("code", "first_name", "last_name", "team", "nationality")
    search_fields = ("code", "first_name", "last_name", "team", "nationality")
    list_filter = ("team", "nationality")
