from rest_framework import viewsets

from . models import Comments, Review
from .serializers import CommentsSerializer, ReviewSerializer
from .tasks import update_event_rating


class CommentsViewSet(viewsets.ModelViewSet):
     queryset = Comments.objects.all()
     serializer_class = CommentsSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        event_id = response.data.get('event')  # Получите event_id из созданного отзыва
        update_event_rating.delay(event_id)  # Запустите задачу Celery для обновления рейтинга
        return response



