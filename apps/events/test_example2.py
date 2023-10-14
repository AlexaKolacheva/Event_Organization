from django.test import TestCase

from datetime import timedelta
from unittest.mock import patch

import pytest
from rest_framework import status
from rest_framework.response import Response

from .models import Category, CustomUser
from .serializers import EventSerializer
from .views import EventViewSet

@pytest.mark.django_db
@patch('apps.events.tasks.send_event_reminder_notification.apply_async')
def test_perform_create(mock_apply_async):
    category = Category.objects.create(category_name='Test Category')  # Создаем тестовую категорию
    owner = CustomUser.objects.create(username='testuser')  # Создаем тестового пользователя

    data = {
        'event_name': 'Блошиный рынок',
        'description': 'Большая распродажа винтажных и раритетных вещей',
        'date_start': '2023-10-15',
        'event_place': 'Рынок Жеысу',
        'category': category.id,  # Передаем ID категории
        'owner': owner.id  # Передаем ID владельца
    }

    serializer = EventSerializer(data=data)
    assert serializer.is_valid(), serializer.errors

    view = EventViewSet()
    response = view.perform_create(serializer)

    assert mock_apply_async.called
    call_args = mock_apply_async.call_args
    assert call_args[0][0][0] == serializer.instance.id
    assert 'eta' in call_args[1]

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == serializer.data
