from rest_framework import serializers
from .models import Comments, Review
from .tasks import update_event_rating


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('author', 'event_comment', 'text')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('user', 'event', 'rating', 'text')


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        event_id = response.data.get('event')
        update_event_rating.delay(event_id)
        return response


