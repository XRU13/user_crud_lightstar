from sqlalchemy.orm import registry
from app.domain.models.user import User
from app.domain.models.tables import users

mapper_registry = registry()

mapper_registry.map_imperatively(User, users)
