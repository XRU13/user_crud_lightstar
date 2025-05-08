from typing import AsyncGenerator

from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.repositories.abstract.user_repository import IUserRepository
from app.domain.repositories.user_repository import UserRepository
from app.domain.services.user import UserService
from app.infrastructure.database.session import async_session


async def provide_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Provide database session."""
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def provide_user_repository(
    session: AsyncSession,
) -> AsyncGenerator[IUserRepository, None]:
    """Provide user repository."""
    yield UserRepository(session)


async def provide_user_service(
    repository: IUserRepository,
) -> AsyncGenerator[UserService, None]:
    """Provide user service."""
    yield UserService(repository)


db_session = Provide(provide_db_session)
user_repository = Provide(provide_user_repository)
user_service = Provide(provide_user_service)
