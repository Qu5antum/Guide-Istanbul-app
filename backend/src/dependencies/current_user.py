from fastapi import Depends, HTTPException, status
from backend.src.database.db import get_session, AsyncSession
from backend.src.models.models import User
from backend.src.security.security import get_user_from_token
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# get currect user
async def get_current_user(
    user_id: int = Depends(get_user_from_token),
    session: AsyncSession = Depends(get_session)
)-> User:
    user = await session.get(User, int(user_id))

    result = await session.execute(
        select(User)
        .where(User.id == user.id)
        .options(selectinload(User.roles)) 
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Пользовтель не найден.")
    return user