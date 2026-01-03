from backend.src.database.db import AsyncSession
from backend.src.models.models import Review
from fastapi import HTTPException, status
from sqlalchemy import select

async def get_all_reviews(
        session: AsyncSession,
        review_id: int
):
    if review_id:
        review = await session.get(Review, review_id)

        if not review:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Коментарии не найден."
            )
        result = await session.execute(
            select(Review).where(Review.id == review_id)
        )
    else:
        result = await session.execute(
            select(Review)
        )

    return result.scalars().all()

    

async def delete_review_by_id(
        session: AsyncSession,
        review_id: int,
):
    review = await session.get(Review, review_id)

    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Коментарии не найден."
        )
    
    await session.delete(review)
    await session.commit()

    return {"detail": "Комментарий успешно удалён"}