from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from litestar import Litestar, Request
from litestar.response import Response
from litestar.config.cors import CORSConfig
from litestar.openapi import OpenAPIConfig
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR

from app.domain.models.tables import metadata
from app.domain.repositories.abstract.user_repository import IUserRepository
from app.domain.services.user import UserService
from app.infrastructure.database.session import engine
from app.interfaces.api.user_router import UserController

cors_config = CORSConfig(allow_origins=["*"])

openapi_config = OpenAPIConfig(
    title="User CRUD API",
    version="1.0.0",
    description="A simple CRUD API for managing users",
)


async def init_db() -> None:
    """Initialize the database."""
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


async def on_startup() -> None:
    """Startup event handler."""
    await init_db()


async def exception_handler(request: Request, exc: Exception) -> Response[Any]:
    """Handle exceptions."""
    if isinstance(exc, HTTPException):
        return Response(
            status_code=exc.status_code,
            content={"detail": exc.detail},
        )
    return Response(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )


app = Litestar(
    route_handlers=[UserController],
    cors_config=cors_config,
    openapi_config=openapi_config,
    on_startup=[on_startup],
    signature_namespace={
        "AsyncSession": AsyncSession,
        "IUserRepository": IUserRepository,
        "UserService": UserService,
    },
    exception_handlers={Exception: exception_handler},
)
