from django.test import TestCase

from datetime import timedelta
from unittest.mock import patch

import pytest
from rest_framework import status
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate, APIClient
from rest_framework.response import Response

from .models import Category, CustomUser
from .serializers import EventSerializer
from .views import EventViewSet

# @pytest.mark.django_db
# @patch('apps.events.tasks.send_event_reminder_notification.apply_async')
# def test_perform_create(mock_apply_async):
#     category = Category.objects.create(category_name='Test Category')  # Создаем тестовую категорию
#     owner = CustomUser.objects.create(username='testuser')  # Создаем тестового пользователя
#
#     data = {
#         'event_name': 'Блошиный рынок',
#         'description': 'Большая распродажа винтажных и раритетных вещей',
#         'date_start': '2023-10-15',
#         'event_place': 'Рынок Жеысу',
#         'category': category.id,  # Передаем ID категории
#         'owner': owner.id  # Передаем ID владельца
#     }
#
#     serializer = EventSerializer(data=data)
#     assert serializer.is_valid(), serializer.errors
#
#     view = EventViewSet()
#     response = view.perform_create(serializer)
#
#     assert mock_apply_async.called
#     call_args = mock_apply_async.call_args
#     assert call_args[0][0][0] == serializer.instance.id
#     assert 'eta' in call_args[1]
#
#     assert response.status_code == status.HTTP_201_CREATED
#     assert response.data == serializer.data


User = get_user_model()

@pytest.fixture
def user():
    return User.objects.create_user(email='user@example.com', password='password123')

@pytest.fixture
def other_user():
    return User.objects.create_user(email='other@example.com', password='password456')

@pytest.fixture
def api_client():
    return APIClient()
@pytest.mark.django_db
def test_owner_can_modify_own_profile(api_client, user, other_user):
    # Авторизуем пользователя
    api_client.force_authenticate(user=user)

    # Попытка изменить свой профиль
    response = api_client.put(f'/api/auth/users/{user.id}/', {'email': 'newemail@example.com'})
    assert response.status_code == status.HTTP_200_OK

    # Попытка изменить профиль другого пользователя
    response = api_client.put(f'/api/auth/users/{other_user.id}/', {'email': 'newemail@example.com'})
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_unauthenticated_user_cannot_modify_profile(api_client, user):
    # Попытка изменить профиль без аутентификации
    response = api_client.put(f'/api/auth/users/{user.id}/', {'email': 'newemail@example.com'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_owner_can_view_own_profile(api_client, user):
    # Авторизуем пользователя
    api_client.force_authenticate(user=user)

    # Просмотр своего профиля
    response = api_client.get(f'/api/auth/users/{user.id}/')
    assert response.status_code == status.HTTP_200_OK



