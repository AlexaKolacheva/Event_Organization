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
    category = CategorySerializer()  # Вложенный сериализатор для связанной модели Category
    owner = CustomUserSerializer()  # Вложенный сериализатор для связанной модели CustomUser

    class Meta:
        model = Event
        fields = ('id', 'event_name', 'description', 'date_start', 'event_place', 'category', 'image', 'owner')

class CommentsSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()  # Вложенный сериализатор для связанной модели CustomUser
    event_comment = EventSerializer()  # Вложенный сериализатор для связанной модели Event

    class Meta:
        model = Comments
        fields = ('id', 'author', 'event_comment', 'text', 'datetime')

class ParticipationSerializer(serializers.ModelSerializer):
    participation_event = EventSerializer()  # Вложенный сериализатор для связанной модели Event
    participation_user = CustomUserSerializer()  # Вложенный сериализатор для связанной модели CustomUser

    class Meta:
        model = Participation
        fields = ('id', 'participation_event', 'status', 'participation_user')


