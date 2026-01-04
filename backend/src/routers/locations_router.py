from fastapi import APIRouter, Depends, status
from backend.src.services.locations_service import get_all_locations, search_location_by_title
from backend.src.dependencies.check_role import require_roles
from backend.src.database.db import AsyncSession, get_session

router = APIRouter(
    prefix="/location",
    tags=["locations"]
)

@router.get("/", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def get_locations(
    session: AsyncSession = Depends(get_session)
):
    return await get_all_locations(session=session)


@router.get("/search", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def search_locations(
    title: str,
    session: AsyncSession = Depends(get_session)
):
    return await search_location_by_title(session=session, title=title)


