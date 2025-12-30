from backend.src.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    username: Mapped[int] = mapped_column(unique=True)
    email: Mapped[int] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(index=True)
    #add roles to database
    