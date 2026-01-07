from backend.src.database.db import AsyncSession, get_session
from fastapi import APIRouter, Depends, status
from backend.src.api.dependencies.check_role import require_roles
from backend.src.api.dependencies.current_user import get_current_user
from backend.src.models.models import User
from backend.src.services.ai_sevice.save_message import save_chat_message
from backend.src.services.ai_sevice.ai_responce import ai_response


router = APIRouter(
    prefix="/ai_assistant",
    tags=["ai"]
)


@router.post("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def get_ai_message(
    user_prompt: str,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    await save_chat_message(session=session, user_id=user.id, content=user_prompt, role="user")

    ai_message_response = await ai_response(user_prompt=user_prompt)

    await save_chat_message(session=session, user_id=user.id, content=ai_message_response, role="assistant")

    await session.commit()

    return {"answer: ", ai_message_response}


    