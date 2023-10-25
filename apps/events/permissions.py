from rest_framework import permissions, status
from rest_framework.response import Response

from .models import CustomUser

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id



class IsEventOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.participation_event.owner == request.user


class IsEventCreatorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        if request.user and request.user.is_authenticated:
            return True
        return Response({'detail': 'Вы должны быть аутентифицированы для выполнения этого действия.'},
                        status=status.HTTP_401_UNAUTHORIZED)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
