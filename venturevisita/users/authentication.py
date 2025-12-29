from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import AuthToken

class TokenAuthentication(BaseAuthentication):
    keyword = 'Token'
    def authenticate(self, request):
        auth = request.headers.get('Authorization')
        if not auth:
            return None
        parts = auth.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            return None
        key = parts[1]
        try:
            token = AuthToken.objects.select_related('user').get(key=key)
        except AuthToken.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')
        return (token.user, token)
    