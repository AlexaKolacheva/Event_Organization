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


    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        event_id = review.event.id  # Получить идентификатор события из сохраненного объекта Review
        update_event_rating.delay(event_id)
        return review


