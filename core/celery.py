import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-reminder-email': {
        'task': 'apps.events.tasks.send_event_reminder_notification',
        'schedule': crontab(hour=10, minute=10),

    },
}