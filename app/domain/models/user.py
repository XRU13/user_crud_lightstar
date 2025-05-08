from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    """User model."""
    id: int | None = None
    name: str = ""
    surname: str = ""
    password: str = ""
    created_at: datetime | None = None
    updated_at: datetime | None = None
