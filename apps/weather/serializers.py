from rest_framework import serializers

from weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('date', 'status', 'temperature', 'weather_description')

