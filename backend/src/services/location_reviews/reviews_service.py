from backend.src.database.db import AsyncSession
from sqlalchemy import select
from backend.src.models.models import Location, Review
from fastapi import HTTPException, status, Depends


# adding a new comment from a user by location id
async def create_new_review(
        session: AsyncSession, 
        user: str,
        data: str
    ):
    location = await session.get(Location, data.location_id)
    
    if not location:
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

# update review(comment)
async def update_review_by_id(
        session: AsyncSession,
        review_id: int,
        user: str,
        data: str
):
    review = await session.get(Review, review_id)

    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Коментарии не найден."
        )
    
    if review.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Вы не можете редактировать чужой комментарий"
        )
    
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(review, field, value)

    await session.commit()
    await session.refresh(review)

    return {"Ваш коментарии был успешно измнен."}

async def get_reviews_by_location_id(
        session: AsyncSession,
        location_id: int
):
    location = await session.get(Location, location_id)
    
    if not location:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Локация по этому id не найдена."
        )
    
    result = await session.execute(
        select(Review)
        .where(Review.location_id == location_id)
    )

    return result.scalars().all()

    

    

    


    
    
    




    