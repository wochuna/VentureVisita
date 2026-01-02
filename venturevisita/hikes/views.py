from rest_framework import viewsets
from .models import Hike
from .serializers import HikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from users.authentication import TokenAuthentication
from .permissions import IsProviderOrReadOnly



class HikeViewSet(viewsets.ModelViewSet):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsProviderOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        if getattr(user, "role", None) != "provider":
            raise PermissionDenied("Only providers can create hikes.")
        serializer.save(provider=user)

    def perform_update(self, serializer):
        obj = self.get_object()
        user = self.request.user
        try:
            owner_matches = obj.provider == user
        except Exception:
            owner_matches = getattr(obj, "provider", None) == getattr(user, "username", None)
        if not owner_matches:
            raise PermissionDenied("Only the provider who created this hike can update it.")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        try:
            owner_matches = instance.provider == user
        except Exception:
            owner_matches = getattr(instance, "provider", None) == getattr(user, "username", None)
        if not owner_matches:
            raise PermissionDenied("Only the provider who created this hike can delete it.")
        instance.delete()
