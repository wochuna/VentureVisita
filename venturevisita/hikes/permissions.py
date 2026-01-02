from rest_framework import permissions

class IsProviderOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        if request.method == 'POST':
            return bool(request.user and request.user.is_authenticated and getattr(request.user, "role", "") == "provider")

        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            return obj.provider == request.user
        except Exception:
            return getattr(obj, "provider", None) == getattr(request.user, "username", None)
        