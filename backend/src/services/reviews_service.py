from backend.src.database.db import AsyncSession
from sqlalchemy import select
from backend.src.models.models import Location, Review
from backend.src.schemas.schemas import ReviewCreate
from fastapi import HTTPException, status, Depends


async def create_new_review(
        session: AsyncSession, 
        user: str,
        data: str
    ):
    location = await session.get(Location, data.location_id)
    
    if location is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Локация по этому id не найдена."
        )
    
    new_review = Review(
        text=data.text,
        rating=data.rating,
        user_id=user.id,
        location_id=data.location_id
    )

    session.add(new_review)
    await session.commit()
    await session.refresh(new_review)

    return {f"Пользователь {user.username}, оставил коментарии {new_review.text}"}




    