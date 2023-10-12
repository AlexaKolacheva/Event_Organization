from rest_framework import serializers
from .models import Comments, Review


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'author', 'event_comment', 'text', 'datetime')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'user', 'event', 'rating', 'text', 'created_at')


