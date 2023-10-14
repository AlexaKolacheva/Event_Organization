from rest_framework import permissions

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
        # Разрешить POST запрос всем пользователям
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:

            return True
        return obj.owner == request.user
