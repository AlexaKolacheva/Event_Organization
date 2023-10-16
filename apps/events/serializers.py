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
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    #owner= serializers.StringRelatedField()
    #category = serializers.StringRelatedField()
    class Meta:
        model = Event
        fields = '__all__'


    def create(self, validated_data):
        if 'image' in validated_data and validated_data['image']:
            # Если поле 'image' присутствует в validated_data и не является пустым
            obj = super().create(validated_data)
            process_image.delay(base64.b64encode(obj.image.read()).decode('utf-8'))
            return obj
        else:
            # Если поле 'image' отсутствует или пусто, просто создаем объект без запуска задачи
            obj = super().create(validated_data)
            return obj


class ParticipationSerializer(serializers.ModelSerializer):
    # participation_user = serializers.StringRelatedField(many=True)
    # participation_event = serializers.StringRelatedField()

    class Meta:
        model = Participation
        fields = '__all__'

