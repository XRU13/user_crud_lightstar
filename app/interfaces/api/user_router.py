from typing import List

from litestar import Controller, get, post, put, delete
from litestar.di import Provide

from app.domain.services.user import UserService
from app.infrastructure.database.dependencies import (
    provide_db_session,
    provide_user_repository,
    provide_user_service,
)
from app.interfaces.api.schemas import UserCreate, UserResponse, UserUpdate


class UserController(Controller):
    """Controller for user operations."""

    path = "/users"
    dependencies = {
        "session": Provide(provide_db_session),
        "repository": Provide(provide_user_repository),
        "service": Provide(provide_user_service),
    }

    @post()
    async def create_user(
        self,
        service: UserService,
        data: UserCreate,
    ) -> UserResponse:
        """Create a new user."""
        user = await service.create(
            name=data.name,
            surname=data.surname,
            password=data.password,
        )
        return UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @get()
    async def list_users(
        self,
        service: UserService,
    ) -> List[UserResponse]:
        """List all users."""
        users = await service.get_all()
        return [
            UserResponse(
                id=user.id,
                name=user.name,
                surname=user.surname,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]

    @get("/{user_id:int}")
    async def get_user(
        self,
        service: UserService,
        user_id: int,
    ) -> UserResponse:
        """Get a user by ID."""
        user = await service.get_by_id(user_id)
        return UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @put("/{user_id:int}")
    async def update_user(
        self,
        service: UserService,
        user_id: int,
        data: UserUpdate,
    ) -> UserResponse:
        """Update a user."""
        update_data = data.model_dump(exclude_none=True)
        user = await service.update(user_id=user_id, **update_data)
        return UserResponse(
            id=user.id,
            name=user.name,
            surname=user.surname,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @delete("/{user_id:int}")
    async def delete_user(
        self,
        service: UserService,
        user_id: int,
    ) -> None:
        """Delete a user."""
        await service.delete(user_id)
