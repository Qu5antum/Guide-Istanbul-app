from backend.src.database.db import AsyncSession
from backend.src.models.models import AiMessages
from sqlalchemy import delete, select
from fastapi import HTTPException, status


# delete history by user_id
async def delete_chat_history(
        session: AsyncSession,
        user_id: int
):
    query = (
        select(AiMessages)
        .where(AiMessages.user_id == user_id)
    )

    await session.delete(query)

    return {"message", "Chat history deleted."}

