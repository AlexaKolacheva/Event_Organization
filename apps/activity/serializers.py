from rest_framework import serializers
from .models import Comments, Review


class CommentsSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # event_comment = serializers.StringRelatedField()
    class Meta:
        model = Comments
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # event = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'


