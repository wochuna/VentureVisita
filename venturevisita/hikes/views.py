from django.shortcuts import render
from rest_framework import viewsets
from .models import Hike
from .serializers import HikeSerializer
from rest_framework.permissions import IsAuthenticated

class HikeViewSet(viewsets.ModelViewSet):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
    permission_classes = [IsAuthenticated]
