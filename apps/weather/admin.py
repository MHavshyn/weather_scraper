from django.contrib import admin

from apps.weather.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ("date",)
    list_filter = ("date",)
    fields = ("date", "status")