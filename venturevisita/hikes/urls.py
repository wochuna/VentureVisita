from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HikeViewSet

router = DefaultRouter()
router.register(r'hikes', HikeViewSet, basename='hike')

urlpatterns = router.urls
