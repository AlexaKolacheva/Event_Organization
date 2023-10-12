from rest_framework import serializers
from .models import CustomUser, Category, Event, Participation

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    # owner = serializers.StringRelatedField()
    # category = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = '__all__'



class ParticipationSerializer(serializers.ModelSerializer):
    # participation_user = serializers.StringRelatedField(many=True)
    # participation_event = serializers.StringRelatedField()

    class Meta:
        model = Participation
        fields = '__all__'

