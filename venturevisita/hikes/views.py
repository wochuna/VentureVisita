from rest_framework import viewsets
from .models import Hike
from .serializers import HikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from users.authentication import TokenAuthentication


class HikeViewSet(viewsets.ModelViewSet):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if getattr(user, "role", None) != "provider":
            raise PermissionDenied("Only providers can create hikes.")
        serializer.save(provider=user)

