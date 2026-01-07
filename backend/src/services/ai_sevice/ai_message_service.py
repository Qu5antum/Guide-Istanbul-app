from backend.src.database.db import AsyncSession
from backend.src.models.models import AiMessages
from sqlalchemy import select


# save user and assistant messages in ai chat
async def save_chat_message(
        session: AsyncSession,
        user_id: int,
        content: str,
        role: str
):
    session.add(AiMessages(
        user_id=user_id,
        role=role,
        content=content
    ))

    await session.commit()



async def get_messages_by_user_id(
        session: AsyncSession,
        user_id: int
):
    result = await session.execute(
        select(AiMessages)
        .where(user_id == user_id)
        .order_by(AiMessages.timestamp)
        .limit(10)
    )

    return result.scalars().all()









    

    

    






    
