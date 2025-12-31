from backend.src.database.db import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.src.models.models import User, Role
from fastapi import HTTPException

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

