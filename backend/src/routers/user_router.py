from backend.src.services.user_service import add_new_user
from fastapi import APIRouter, status, Depends
from backend.src.database.db import AsyncSession, get_session
from backend.src.schemas.schemas import UserCreate
from backend.src.security.security import OAuth2PasswordRequestForm
from backend.src.security.authenticate import auth_user

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.post("/register", status_code=status.HTTP_200_OK)
async def register_new_user(
    user_create: UserCreate, 
    session: AsyncSession = Depends(get_session)
):
    return await add_new_user(session=session, user_create=user_create)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(
    credents: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session)
):
    return await auth_user(credents=credents, session=session)
