from backend.src.database.db import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from backend.src.models.models import Location, LocationType


async def get_types(
        session: AsyncSession,
):
    result = await session.execute(
        select(LocationType).order_by(LocationType.name)
    )
    return result.scalars().all()



async def get_all_locations(session: AsyncSession):
    result = await session.execute(
        select(Location)
        .options(selectinload(Location.types))
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


# filter locations by category(type)
async def get_location_by_category(
        session: AsyncSession,
        type_name: str
):
    result = await session.execute(
        select(LocationType)
        .where(LocationType.name == type_name)
    )

    existing_type = result.scalar_one_or_none()

    if not existing_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No type found by category."
        )


    result = await session.execute(
        select(Location)
        .where(
            Location.types.any(LocationType.id == existing_type.id)
        )
        .options(selectinload(Location.types))
    )

    existing_location = result.scalars().all()

    if not existing_location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No locations found for this category."
        )
    
    return existing_location


    
    
    
    