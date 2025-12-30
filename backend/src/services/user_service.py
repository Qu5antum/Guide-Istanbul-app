from backend.src.database.db import AsyncSession
from backend.src.schemas.schemas import UserCreate
from sqlalchemy import select
from backend.src.models.models import User
from fastapi import HTTPException, status
from backend.src.security.security_context import hash_password

async def add_new_user(session: AsyncSession, user_create: UserCreate):
    query = select(User).where(User.username == user_create.username)
    result = await session.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user: 
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с этим именем уже существует"
        ) 
    
    new_user = User(
        username = user_create.username,
        email = user_create.email,
        password = hash_password(user_create.password)
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return {"message: ", "Успешно зарегистрирован.", new_user}