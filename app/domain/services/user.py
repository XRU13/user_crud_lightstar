from typing import Optional

from app.domain.models.user import User
from app.domain.repositories.abstract.user_repository import IUserRepository
from app.infrastructure.exceptions import NotFoundError


class UserService:
    """User service implementation."""

    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    async def get_by_id(self, user_id: int) -> User:
        """Get user by id."""
        user = await self._user_repository.get_by_id(user_id)
        if not user:
            raise NotFoundError(f"User with id {user_id} not found")
        return user

    async def get_all(self) -> list[User]:
        """Get all users."""
        return await self._user_repository.get_all()

    async def create(self, name: str, surname: str, password: str) -> User:
        """Create user."""
        user = User(
            name=name,
            surname=surname,
            # В реальном приложении здесь должно быть хеширование пароля
            password=password,
        )
        return await self._user_repository.create(user)

    async def update(
        self,
        user_id: int,
        name: Optional[str] = None,
        surname: Optional[str] = None,
        password: Optional[str] = None,
    ) -> User:
        """Update user."""
        user = await self.get_by_id(user_id)

        if name is not None:
            user.name = name
        if surname is not None:
            user.surname = surname
        if password is not None:
            # В реальном приложении здесь должно быть хеширование пароля
            user.password = password

        return await self._user_repository.update(user)

    async def delete(self, user_id: int) -> None:
        """Delete user."""
        deleted = await self._user_repository.delete(user_id)
        if not deleted:
            raise NotFoundError(f"User with id {user_id} not found") 
