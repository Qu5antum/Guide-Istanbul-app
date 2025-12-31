from backend.src.database.db import AsyncSession
from backend.src.models.models import LocationType, Location
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

# add new types for locations
async def add_type(
        session: AsyncSession, 
        type_create: str
):
    try:
        location_type = LocationType(**type_create.model_dump())
        session.add(location_type)
        await session.commit()
        await session.refresh(location_type)
        return location_type
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Такой тип локации уже существует"
    )

async def get_types(
        session: AsyncSession,
):
    result = await session.execute(
        select(LocationType).order_by(LocationType.name)
    )
    return result.scalars().all()
    

# add new location
async def add_location(
        session: AsyncSession,
        location_create: str
):
    query = select(Location).where(Location.location_title == location_create.location_title)
    result = await session.execute(query)
    existing_title = result.scalar_one_or_none()

    if existing_title: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Локация с таким заголовком уже существует."
        )
    
    type_result = await session.execute(
        select(LocationType).where(
            LocationType.id.in_(location_create.type_ids)
        )
    )

    types = type_result.scalars().all() 

    if len(types) != len(set(location_create.type_ids)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Один или несколько типов локации не существуют"
        )
    
    
    location = Location(
        location_title=location_create.location_title,
        description=location_create.description,
        price=location_create.price,
        latitude=location_create.latitude,
        longitude=location_create.longitude,
        link=location_create.link,
    )

    location.types = types

    session.add(location)
    await session.commit()
    await session.refresh(location)

    return location
    

    
