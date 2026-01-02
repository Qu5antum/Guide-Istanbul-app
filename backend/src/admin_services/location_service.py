from backend.src.database.db import AsyncSession
from backend.src.models.models import LocationType, Location
from fastapi import HTTPException, status
from sqlalchemy import select, update
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
    
    data = location_create.model_dump(mode="json", exclude={"type_ids"})
    location = Location(**data)

    location.types = types

    session.add(location)
    await session.commit()
    await session.refresh(location)

    return location

# update location
async def update_location_by_id(
        session: AsyncSession, 
        location_id: int,
        location_update: str
):
    existing_location = await session.get(Location, location_id)

    if not existing_location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Локация по этому id не найдено."
        )
    
    data = location_update.model_dump(
        exclude_unset=True,
        exclude={"types_id"}
    )

    for field, value in data.items():
        setattr(existing_location, field, value)

    if location_update.types_ids is not None:
        result = await session.execute(
            select(LocationType)
            .where(LocationType.id.in_(location_update.types_ids))
        )

        types = result.scalars().all()

        if len(types) != len(set(location_update.type_ids)):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Один или несколько типов локации не существуют"
            )

        existing_location.types = types

    await session.commit()
    await session.refresh(existing_location)

    return existing_location
    


    



    
    

    
