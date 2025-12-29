from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User,AuthToken
from .serializers import UserSerializer, UserRegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from rest_framework.authentication import TokenAuthentication

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create token for newly registered user
        key = get_random_string(40)
        AuthToken.objects.create(user=user, key=key)
        
        data = {"user": UserSerializer(user).data, "token": key}
        return Response(data, status=status.HTTP_201_CREATED)
    
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # remove existing tokens and create a new one
        AuthToken.objects.filter(user=user).delete()
        key = get_random_string(40)
        token = AuthToken.objects.create(user=user, key=key)
        return Response({"token": token.key, "user": UserSerializer(user).data}, status=status.HTTP_200_OK)
    
class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = request.auth
        if token:
            AuthToken.objects.filter(key=getattr(token, "key", None)).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    