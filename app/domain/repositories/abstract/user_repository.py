from abc import ABC, abstractmethod
from typing import List

from app.domain.models.user import User


class IUserRepository(ABC):
    """Abstract user repository."""

    @abstractmethod
    async def get_by_id(self, user_id: int) -> User | None:
        """Get user by id."""
        ...

    @abstractmethod
    async def get_all(self) -> List[User]:
        """Get all users."""
        ...

    @abstractmethod
    async def create(self, user: User) -> User:
        """Create user."""
        ...

    @abstractmethod
    async def update(self, user: User) -> User:
        """Update user."""
        ...

    @abstractmethod
    async def delete(self, user_id: int) -> bool:
        """Delete user."""
        ...
