import requests

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class AuthenticatedUser:
    """Обёртка над данными пользователя из auth-сервиса,
    чтобы DRF мог работать с ними как с объектом пользователя."""

    is_authenticated = True
    is_anonymous = False

    def __init__(self, data: dict):
        self.id = data.get("id")
        self.user_name = data.get("user_name")
        self.is_official = data.get("is_official", False)

    def __str__(self):
        return self.user_name


class AuthServiceAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None

        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            raise AuthenticationFailed("Неверный формат токена")

        response = requests.get(
            "http://127.0.0.1:8001/auth/verify/",
            headers={"Authorization": f"Bearer {token}"}
        )

        if response.status_code != 200:
            raise AuthenticationFailed("Токен недействителен")

        user_data = response.json()
        user = AuthenticatedUser(user_data)

        return (user, None)