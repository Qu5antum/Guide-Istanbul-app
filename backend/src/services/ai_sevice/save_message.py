from backend.src.database.db import AsyncSession
from backend.src.models.models import AiMessages


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









    

    

    






    
