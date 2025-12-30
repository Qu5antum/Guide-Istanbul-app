from fastapi import HTTPException, status, Depends
from sqlalchemy import select
from backend.src.security.security import create_jwt_token, OAuth2PasswordRequestForm
from backend.src.database.db import AsyncSession
from backend.src.security.security_context import check_hashes
from backend.src.models.models import User

#import User from models

async def auth_user(credents: OAuth2PasswordRequestForm, session: AsyncSession):
    query = select(User).where(User.username == credents.username)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден."
        )
    
    if not check_hashes(credents.password, user.password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Неверный пароль."
        )
    
    token = await create_jwt_token({"sub": str(user.id)})
    return {"access_token": token}