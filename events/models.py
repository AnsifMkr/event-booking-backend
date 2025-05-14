# events/models.py

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    date        = models.DateField()
    time        = models.TimeField()
    location    = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    event      = models.ForeignKey(Event, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')