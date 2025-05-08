from typing import List

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.user import User
from app.domain.repositories.abstract.user_repository import IUserRepository


class UserRepository(IUserRepository):
    """User repository implementation."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize repository."""
        self._session = session

    async def get_by_id(self, user_id: int) -> User | None:
        """Get user by id."""
        result = await self._session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_all(self) -> List[User]:
        """Get all users."""
        result = await self._session.execute(select(User))
        return list(result.scalars().all())

    async def create(self, user: User) -> User:
        """Create user."""
        user_data = insert(User).values(
            name=user.name,
            surname=user.surname,
            password=user.password,
        ).returning(User)
        result = await self._session.execute(user_data)
        return result.scalar_one()

    async def update(self, user: User) -> User:
        """Update user."""
        user_data = (
            update(User)
            .where(User.id == user.id)
            .values(
                name=user.name,
                surname=user.surname,
            )
            .returning(User)
        )
        result = await self._session.execute(user_data)
        return result.scalar_one()

    async def delete(self, user_id: int) -> bool:
        """Delete user."""
        stmt = delete(User).where(User.id == user_id)
        result = await self._session.execute(stmt)
        return result.rowcount > 0 
    