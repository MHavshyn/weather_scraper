import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', "weatherscraper.settings")

app = Celery('weatherscraper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run weather scraper every day at 9AM': {
        'task': 'apps.weather.task.scrap_weather',
        'schedule': crontab(hour=9, minute=0),
    }
}
