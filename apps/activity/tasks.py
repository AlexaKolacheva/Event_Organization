from celery import shared_task
from django.db.models import Avg

from .models import Review
from ..events.models import Event


@shared_task
def update_event_rating(event_id):
    reviews = Review.objects.filter(event_id=event_id)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    event = Event.objects.get(id=event_id)
    event.average_rating = average_rating
    event.save()

    return f"Рейтинг  {event_id}: {average_rating}"