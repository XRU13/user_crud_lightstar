from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    """User base schema."""
    name: str
    surname: str


class UserCreate(UserBase):
    """User create schema."""
    password: str


class UserUpdate(BaseModel):
    """User update schema."""
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    """User response schema."""
    # password: str если не нужно возвращать пароль
    id: int
    created_at: datetime
    updated_at: datetime 
    