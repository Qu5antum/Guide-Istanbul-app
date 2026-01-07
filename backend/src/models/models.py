from backend.src.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, DateTime, Text, func
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(index=True, nullable=False)

    roles: Mapped[list["Role"]] = relationship(
        secondary="user_roles",
        back_populates="users"
    )

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    ai_messages: Mapped[list["AiMessages"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    users: Mapped[list["User"]] = relationship(
        secondary="user_roles",
        back_populates="roles"
    )

# many to many User <-> Role
user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


class AiMessages(Base):
    __tablename__ = "aibot_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String, 
        nullable=False
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    user: Mapped["User"] = relationship(back_populates="ai_messages")



class Location(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    location_title: Mapped[str] = mapped_column(String, index=True, nullable=False)
    link: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[str] = mapped_column(String, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    adres: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    
    types: Mapped[list["LocationType"]] = relationship(
        secondary="location_type_link",
        back_populates="locations"
    )

    reviews: Mapped[list["Review"]] = relationship(
        back_populates="location",
        cascade="all, delete-orphan"
    )

class LocationType(Base):
    __tablename__ = "location_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)

    locations: Mapped[list["Location"]] = relationship(
        secondary="location_type_link",
        back_populates="types"
    )
    
location_type_link = Table(
    "location_type_link",
    Base.metadata,
    Column("location_id", ForeignKey("locations.id", ondelete="CASCADE")),
    Column("type_id", ForeignKey("location_types.id", ondelete="CASCADE")),
)


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE")
    )
    location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id", ondelete="CASCADE")
    )

    user: Mapped["User"] = relationship(back_populates="reviews")
    location: Mapped["Location"] = relationship(back_populates="reviews")

