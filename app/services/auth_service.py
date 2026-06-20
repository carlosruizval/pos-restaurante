from models.user import User

MOCK_USERS = [
    User(id="1", name="Admin Demo", role="admin", email="admin@pos.com"),
    User(id="2", name="Mesero Juan", role="mesero", email="juan@pos.com"),
    User(id="3", name="Cajero Ana", role="cajero", email="ana@pos.com"),
]

class AuthService:
    def __init__(self):
        self.current_user: User | None = None

    def login(self, username: str, password: str) -> User | None:
        if username and password:
            self.current_user = MOCK_USERS[0]
            return self.current_user
        return None

    def logout(self):
        self.current_user = None

    def get_current_user(self) -> User | None:
        return self.current_user