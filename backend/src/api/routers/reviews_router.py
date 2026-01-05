from backend.src.database.db import AsyncSession, get_session
from backend.src.api.schemas.schemas import ReviewCreate, ReviewUpdate
from backend.src.models.models import User
from fastapi import HTTPException, status, Depends, APIRouter
from backend.src.api.dependencies.current_user import get_current_user
from backend.src.api.dependencies.check_role import require_roles
from backend.src.services.location_reviews.reviews_service import create_new_review, update_review_by_id
from backend.src.services.location_reviews.reviews_service import get_reviews_by_location_id

router = APIRouter(
    prefix="/location/review",
    tags=["reviews"]
)

@router.get("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def get_review(
    location_id: int,
    sessoin: AsyncSession = Depends(get_session)
):
    return await get_reviews_by_location_id(session=sessoin, location_id=location_id)


@router.post("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def new_review(
    data: ReviewCreate,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    return await create_new_review(session=session, user=user, data=data)


@router.put("/{review_id}", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def update_review(
    data: ReviewUpdate,
    review_id: int,
    user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session)
):
    return await update_review_by_id(session=session, review_id=review_id, user=user, data=data)