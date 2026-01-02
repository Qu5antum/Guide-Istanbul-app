from backend.src.database.db import AsyncSession
from sqlalchemy import select
from backend.src.models.models import Location


async def get_all_locations(session: AsyncSession):
    result = await session.execute(
        select(Location)
    )
    return result.scalars().all()