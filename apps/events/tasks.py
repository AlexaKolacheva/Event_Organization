# apps/notifications/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from apps.events.models import Event

@shared_task
def send_event_reminder_notification(event_id):
    try:
        event = Event.objects.get(id=event_id)
        event_date = event.date_start
        notification_date = event_date - timedelta(days=1)
        current_time = timezone.now()

        if notification_date > current_time:
            subject = f'Reminder: {event.event_name}'
            message = f"Don't forget, the event {event.event_name} is tomorrow at {event_date}."
            recipient_list = ['alexakola4eva@gmail.com']

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
            return f"Reminder email sent for event: {event.event_name}"

        return f"No reminder email sent for event: {event.event_name} (event is too close)"
    except Event.DoesNotExist:
        return f"Event with id {event_id} not found"
