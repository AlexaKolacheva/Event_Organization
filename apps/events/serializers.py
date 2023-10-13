from rest_framework import serializers
from .models import CustomUser, Category, Event, Participation
from .tasks import process_image
import base64

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


    def create(self, validated_data):
        obj = super().create(validated_data)
        process_image.delay(base64.b64encode(obj.image.read()).decode('utf-8'))
        return obj


class ParticipationSerializer(serializers.ModelSerializer):
    # participation_user = serializers.StringRelatedField(many=True)
    # participation_event = serializers.StringRelatedField()

    class Meta:
        model = Participation
        fields = '__all__'

