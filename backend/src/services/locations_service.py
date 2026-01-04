from backend.src.database.db import AsyncSession
from sqlalchemy import select
from backend.src.models.models import Location


async def get_all_locations(session: AsyncSession):
    result = await session.execute(
        select(Location)
    )
    return result.scalars().all()


# seacrh location by title | probably i will change this part of code
async def search_location_by_title(
        session: AsyncSession,
        title: str
):
    result = await session.execute(
        select(Location)
        .where(Location.location_title.ilike(f"%{title}%"))
        .order_by(Location.location_title)
        .limit(20)
    )

    return result.scalars().all()
    