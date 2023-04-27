from django.db import models

from model_utils import Choices
from model_utils.fields import StatusField


class Weather(models.Model):
    STATUS = Choices('Scheduled', 'In_Progress', 'Done')

    date = models.CharField(blank=True, null=True, max_length=32)
    status = StatusField(default='Scheduled', choices_name='STATUS', max_length=32, null=True, blank=True)
    temperature = models.CharField(blank=True, null=True, max_length=32)
    weather_description = models.CharField(blank=True, null=True, max_length=512)
