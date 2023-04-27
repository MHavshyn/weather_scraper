import re

from celery import shared_task
import requests
from bs4 import BeautifulSoup
import datetime
import logging
from apps.weather.models import Weather
from weatherscraper.settings import DAYS_TO_PARSE

logging.basicConfig(filename='logs/scrap_weather.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


@shared_task
def scrap_weather():
    """
    The following Celery task runs daily at 9am and scrapes weather information (such as temperature and weather description)
    from https://pogoda.meta.ua for Kyiv. It collects data for today and the next 'DAYS_TO_PARSE' days. By default,
    'DAYS_TO_PARSE' is set to 5.
    """
    try:
        today = datetime.datetime.now().date()
        days = [today + datetime.timedelta(days=i) for i in range(DAYS_TO_PARSE + 1)]
        for day in days:
            Weather.objects.update_or_create(date=day, defaults={'status': Weather.STATUS.In_Progress})

            logging.info('In Progress')

            url = f'https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/{str(day)}/ajax/'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
            response = requests.get(url, headers=headers)

            logging.info(f'response: {response.status_code}')

            soup = BeautifulSoup(response.content, 'html.parser')
            temperature = re.findall(r"[+-]\d+", soup.find('div', {'class': 'city__main-temp'}).text.strip())[0]
            weather_description = soup.find('span', {'class': 'city__main-image-descr'}).text.strip().replace("\n", "")

            logging.info(f'day: {str(day)}, temperature: {temperature}, weather_description: {weather_description} ')

            Weather.objects.filter(date=str(day)).update(
                status=Weather.STATUS.Done,
                temperature=temperature,
                weather_description=weather_description
            )
    except Exception as err:
        logging.error("Error processing scrap_weather: %s", err)
