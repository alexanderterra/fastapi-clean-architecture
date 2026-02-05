from app.core.security import hash_password, verify_password, create_access_token
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, email: str, password: str):
        return self.repo.create(email, hash_password(password))

    def login(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return create_access_token({"sub": str(user.id)})
