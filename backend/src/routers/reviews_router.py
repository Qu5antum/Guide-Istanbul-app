from backend.src.database.db import AsyncSession, get_session
from backend.src.schemas.schemas import ReviewCreate
from backend.src.models.models import User
from fastapi import HTTPException, status, Depends, APIRouter
from backend.src.dependencies.current_user import get_current_user
from backend.src.dependencies.check_role import require_roles
from backend.src.services.reviews_service import create_new_review

router = APIRouter(
    prefix="/review",
    tags=["reviews"]
)


@router.post("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def new_review(
        data: ReviewCreate,
        user: User = Depends(get_current_user),
        session: AsyncSession = Depends(get_session)
):
    return await create_new_review(session=session, user=user, data=data)