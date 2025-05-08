import os
from dataclasses import dataclass, field
from functools import lru_cache


@dataclass
class DatabaseConfig:
    """Database configuration."""
    host: str = os.getenv("DB_HOST", "db")
    port: int = int(os.getenv("DB_PORT", "5432"))
    user: str = os.getenv("DB_USER", "postgres")
    password: str = os.getenv("DB_PASSWORD", "postgres")
    database: str = os.getenv("DB_NAME", "postgres")

    @property
    def url(self) -> str:
        """Get database URL."""
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )


@dataclass
class AppConfig:
    """Application configuration."""
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))


@dataclass
class Config:
    """Application configuration."""
    app: AppConfig = field(default_factory=AppConfig)
    db: DatabaseConfig = field(default_factory=DatabaseConfig)


@lru_cache()
def get_config() -> Config:
    return Config() 
