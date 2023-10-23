from rest_framework import serializers
from .models import CustomUser, Category, Event, Participation
from .tasks import process_image
import base64

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email =validated_data['email'],
            )

        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'category_description')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_name', 'description', 'date_start',
                  'event_place', 'category', 'image', 'owner')

    def create_owner(self, validated_data):

        user = self.context['request'].user
        validated_data['owner'] = user
        event = Event.objects.create(**validated_data)
        return event


    def create(self, validated_data):
        if 'image' in validated_data and validated_data['image']:
            obj = super().create(validated_data)
            process_image.delay(base64.b64encode(obj.image.read()).decode('utf-8'))
            return obj
        else:
            obj = super().create(validated_data)
            return obj


class ParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participation
        fields = ('participation_event', 'status', 'participation_user')

