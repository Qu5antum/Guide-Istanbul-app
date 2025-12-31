from fastapi import APIRouter, Depends
from backend.src.models.models import User
from backend.src.dependencies.check_role import require_roles
from backend.src.admin_services.user_role import get_user_and_check_role
from backend.src.database.db import AsyncSession, get_session

router = APIRouter(
    prefix="/admin_panel",
    tags=["admins"]
)

@router.get("/admin", dependencies=[Depends(require_roles(["admin"]))])
async def mod_endpoint(
    session: AsyncSession = Depends(get_session)
):
    return  await get_user_and_check_role(session=session)