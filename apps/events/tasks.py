# apps/notifications/tasks.py

from celery import shared_task
from django.core.mail import send_mail

from datetime import timedelta
from PIL import Image
from apps.events.models import Event


@shared_task
def send_event_reminder_notification(event_id):
    try:
        event = Event.objects.get(id=event_id)
        event_date = event.date_start
        notification_date = event_date - timedelta(days=1)

        if notification_date :
            subject = f'Напоминание: {event.event_name}'
            message = f"Не забудьте,  {event.event_name} будет  {event_date}."
            recipient_list = ['alexakola4eva@gmail.com']

            send_mail(subject, message, 'alexakola4eva@gmail.com', recipient_list)
            return f"Напоминание: {event.event_name}"

        return f"No reminder email sent for event: {event.event_name} (event is too close)"
    except Event.DoesNotExist:
        return f"Event with id {event_id} not found"


@shared_task
def process_image(file_path):
    try:
        with Image.open(file_path) as img:
            img = img.convert('RGB')
            img.thumbnail((800, 600))
            img.save(file_path, optimize=True)

        return f"Image optimized and resized: {'media/apps.events'}"
    except Exception as e:
        return f"Error processing image: {'media/apps.events'}, {str(e)}"