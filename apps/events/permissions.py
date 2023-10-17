from rest_framework import permissions
from .models import CustomUser

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        print(f'Incoming request method: {request.method}, user: {request.user}')

        # Разрешить GET и POST для всех пользователей
        if request.method in ['GET', 'POST']:
            return True
        # Разрешить PUT, PATCH и DELETE только для аутентифицированных пользователей
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print(f'Checking object permission for user: {request.user.id}, object: {obj.id}')
        # Разрешить безопасные методы для всех пользователей
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить PUT, PATCH и DELETE только владельцу профиля
        return obj.id == request.user.id



class IsEventOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешить POST запрос всем пользователям
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешить доступ к участникам события только владельцам события для методов, кроме POST
        if request.method in permissions.SAFE_METHODS:
            # Разрешить GET, HEAD, OPTIONS запросы всем пользователям
            return True
        return obj.participation_event.owner == request.user




class IsEventCreatorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:

            return True
        return obj.owner == request.user
