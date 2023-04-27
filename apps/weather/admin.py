from django.contrib import admin

from apps.weather.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ("date", "status")
    search_fields = ("date",)
    readonly_fields = ("date", "status", "temperature", "weather_description")
