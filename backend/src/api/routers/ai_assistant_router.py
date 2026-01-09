from backend.src.database.db import AsyncSession, get_session
from fastapi import APIRouter, Depends, status, Request
from backend.src.api.dependencies.check_role import require_roles
from backend.src.api.dependencies.current_user import get_current_user
from backend.src.models.models import User
from backend.src.services.ai_sevice.ai_message_service import save_chat_message, get_messages_by_user_id
from backend.src.services.ai_sevice.ai_responce import ai_response
from backend.src.services.ai_sevice.ai_message_service import delete_chat_history
from backend.src.core.tools.calculate_distance_location import calculate_distance

from backend.src.api.schemas.schemas import UserLocation



router = APIRouter(
    prefix="/ai_assistant",
    tags=["ai"]
)


@router.post("/user_location", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def get_ai_message(
    user_prompt: str,
    user_location: UserLocation,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    await save_chat_message(session=session, user_id=user.id, content=user_prompt, role="user")

    ai_message_response = await ai_response(
        f"{user_prompt}. "
        f"My location: latitude {user_location.lat}, longitude {user_location.lon}"
    )



    await save_chat_message(session=session, user_id=user.id, content=ai_message_response, role="assistant")

    return {"answer: ": ai_message_response}



@router.get("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def get_message_history(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    return await get_messages_by_user_id(session=session, user_id=user.id)



@router.delete("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def delete_chat(
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    return await delete_chat_history(session=session, user_id=user.id)
    


    