from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    func,
)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("surname", String(255), nullable=False),
    Column("password", String(255), nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column(
        "updated_at",
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    ),
)
