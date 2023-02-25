import uuid

from django.contrib.auth.models import User
from django.db import models

from events.models import Event


class Booking(models.Model):
    registration_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.username} | {self.event}"
