from fastapi import APIRouter, Depends, status
from backend.src.services.locations_service import get_all_locations, search_location_by_title, get_location_by_category, get_types
from backend.src.api.dependencies.check_role import require_roles
from backend.src.database.db import AsyncSession, get_session

router = APIRouter(
    prefix="/location",
    tags=["locations"]
)


@router.get("/location_type/{type_id}", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def get_location_types(
    session: AsyncSession = Depends(get_session)
):
    return await get_types(session=session)


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


@router.get("/type_name", dependencies=[Depends(require_roles(["user", "admin"]))], status_code=status.HTTP_200_OK)
async def filter_location(
    type_name: str,
    session: AsyncSession = Depends(get_session)
):
    return await get_location_by_category(session=session, type_name=type_name)


