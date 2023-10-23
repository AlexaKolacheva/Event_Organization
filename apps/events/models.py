from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.events.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=55, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name


class Event(models.Model):
    event_name = models.CharField(max_length=155)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_start = models.DateField()
    event_place = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='apps.events', blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name


class Participation(models.Model):
    WILL_GO = 'Will go'
    WONT_GO = "Won't go"
    STILL_THINKING = 'Still thinking...'

    STATUS_CHOICES = [
        (WILL_GO, 'Will go'),
        (WONT_GO, "Won't go"),
        (STILL_THINKING, 'Still thinking...')
    ]

    participation_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=55, choices=STATUS_CHOICES)
    participation_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.participation_user} {self.get_status_display()} in {self.participation_event}'
