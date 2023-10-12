from rest_framework import serializers
from .models import CustomUser, Category, Event, Comments, Participation

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_description')

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('id', 'author', 'event_comment', 'text', 'datetime')

class ParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = ('id', 'participation_event', 'status', 'participation_user')


