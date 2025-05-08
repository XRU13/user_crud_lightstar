"""Infrastructure package."""

from app.infrastructure.config import Config
from app.infrastructure.exceptions import NotFoundError

__all__ = ["Config", "NotFoundError"] 
