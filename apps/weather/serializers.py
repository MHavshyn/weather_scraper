from rest_framework import serializers

from apps.weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    """
        Return all serialized information from the Weather table,
        uses in view: WeatherInfoView
    """
    class Meta:
        model = Weather
        fields = ('date', 'temperature', 'weather_description')


class WeatherChangeInfoSerializer(serializers.ModelSerializer):
    """
        Return 'temperature' and 'weather_description' serialized information from the Weather table,
        uses in view: WeatherChangeInfoView for change information by date

    """
    class Meta:
        model = Weather
        fields = ('temperature', 'weather_description')
