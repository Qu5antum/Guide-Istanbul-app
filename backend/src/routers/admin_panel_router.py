from fastapi import APIRouter, Depends
from backend.src.models.models import User
from backend.src.dependencies.check_role import require_roles

router = APIRouter(
    prefix="/admin_panel",
    tags=["admins"]
)

@router.post("/admin")
async def mod_endpoint(
    current_user: User = Depends(require_roles(["admin"]))
):
    return {"user": current_user.username}