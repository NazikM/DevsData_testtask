from django.db import models
import pandas as pd


class Event(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='event/%Y/%m/%d/', blank=True, verbose_name='thumbnails')

    def __str__(self):
        return f"{self.title} {pd.to_datetime(self.start_date).strftime('%m/%d/%Y %H:%M:%S')}"
