from backend.src.database.db import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.src.models.models import User, Role
from fastapi import HTTPException, status


# get all users
async def get_users_by_id(
        session: AsyncSession,
        user_id: int
):
    if not user_id:
        result = await session.execute(
            select(User)
        )
    else:
        resulst = await session.execute(
            select(User)
            .where(User.id == user_id)
        )

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    return result.scalars().all()




# get all users and filter by roles
async def get_users_roles(
    session: AsyncSession,
    role: str
):
    if role:
        result = await session.execute(
            select(User)
            .options(selectinload(User.roles)) 
            .join(User.roles)
            .where(Role.name == role)
        )
    else:
        result = await session.execute(
            select(User)
            .options(selectinload(User.roles)) 
        )

    return result.scalars().all()

