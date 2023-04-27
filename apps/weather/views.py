from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.weather.task import scrap_weather

from apps.weather.serializers import WeatherSerializer, WeatherChangeInfoSerializer
from apps.weather.models import Weather


class WeatherInfoView(ListAPIView):
    """
        Return a list of JSON objects containing all the serialized information about the Weather table,
        using the WeatherSerializer;
        If the database is empty, return an empty list;
        If an error occurs, return a status code of 404;
        If the request is successful, return a status code of 200.
    """
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()


class WeatherChangeInfoView(UpdateAPIView):
    """
        Used to change temperature and weather description information in the Weather table;
        Returns an object in JSON format that includes the updated temperature and weather description information,
        using the WeatherChangeInfoSerializer;
        If an error occurs (e.g. the date to be changed is invalid or missing in the database), return a status code of 404;
        If the request is successful, return a status code of 200;
        example for date: api/v1/weather/2023-04-27
    """
    serializer_class = WeatherChangeInfoSerializer
    queryset = Weather.objects.all()
    lookup_field = 'date'


class StartWeatherScrapingView(APIView):
    """
        Use this endpoint to manually trigger the scraping of weather data;
        return status code 200.
    """
    @swagger_auto_schema(responses={200: ''})
    def post(self, request):
        scrap_weather.delay()
        return Response(status=status.HTTP_200_OK)
