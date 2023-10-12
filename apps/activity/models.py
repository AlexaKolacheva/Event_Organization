from django.db import models

from apps.events.models import CustomUser, Event


class Comments(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event_comment = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_reviwes')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пользователь {self.user.username} оценил событие {self.event.event_name} на {self.rating}"


