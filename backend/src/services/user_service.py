from backend.src.database.db import AsyncSession
from backend.src.schemas.schemas import UserCreate
from sqlalchemy import select
from backend.src.models.models import User, Role
from fastapi import HTTPException, status
from backend.src.security.security_context import hash_password

async def add_new_user(session: AsyncSession, user_create: UserCreate):
    query = select(User).where(User.username == user_create.username)
    result = await session.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с этим именем уже существует"
        ) 
    
    role = await session.scalar(
        select(Role).where(Role.name == "user") 
    )

    if not role:
        raise ValueError("Role not found")
    
    new_user = User(
        username = user_create.username,
        email = user_create.email,
        password = hash_password(user_create.password),
        roles = [role]
    )

    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    return {"message: ", "Успешно зарегистрирован."}