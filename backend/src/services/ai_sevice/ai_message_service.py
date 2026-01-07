from backend.src.database.db import AsyncSession
from backend.src.models.models import AiMessages
from sqlalchemy import select
from fastapi import HTTPException, status


# save user and assistant messages in ai chat
async def save_chat_message(
        session: AsyncSession,
        user_id: int,
        content: str,
        role: str
):
    try:
        session.add(AiMessages(
            user_id=user_id,
            role=role,
            content=content
        ))

        await session.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



async def get_messages_by_user_id(
        session: AsyncSession,
        user_id: int
):
    try:
        result = await session.execute(
            select(AiMessages)
            .where(user_id == user_id)
            .order_by(AiMessages.timestamp)
            .limit(10)
        )

        return result.scalars().all()
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    









    

    

    






    
