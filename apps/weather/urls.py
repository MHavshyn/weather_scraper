from django.urls import path

from apps.weather.views import WeatherInfoView, WeatherChangeInfoView, StartWeatherScrapingView

urlpatterns = [
    path('', WeatherInfoView.as_view(), name='weather_list'),
    path('reparse', StartWeatherScrapingView.as_view(), name='start_parce'),
    path('<date>', WeatherChangeInfoView.as_view(), name='weather_change'),

]

