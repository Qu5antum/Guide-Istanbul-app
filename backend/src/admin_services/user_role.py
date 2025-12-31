from backend.src.database.db import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.src.models.models import User, Role
from fastapi import HTTPException

async def get_user_and_check_role(
    session: AsyncSession,
):
    result = await session.execute(
        select(User)
        .options(selectinload(User.roles)) 
    )

    return result.scalars().all()

