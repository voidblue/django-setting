from domain.models import User


class UserApplication:
    def __init__(self):
        return

    def create_user(self, username: str, password: str) -> User:
        return User.objects.create_user(username = username, password = password)
