from rest_framework import permissions

class IsReviewOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешить POST запрос всем пользователям
        if request.method == 'POST' or request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешить доступ к участникам события только владельцам события для методов, кроме POST
        if request.method in permissions.SAFE_METHODS:
            # Разрешить HEAD, OPTIONS запросы всем пользователям
            return True
        return obj.event.owner == request.user
