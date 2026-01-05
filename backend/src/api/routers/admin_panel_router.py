from fastapi import APIRouter, Depends, status
from backend.src.api.dependencies.check_role import require_roles
from backend.src.admin_services.user_role import get_users_roles
from backend.src.admin_services.admin_location_service import add_type, add_location, update_location_by_id, delete_locations_by_id
from backend.src.admin_services.admin_reviews_service import delete_review_by_id, get_all_reviews
from backend.src.database.db import AsyncSession, get_session
from backend.src.api.schemas.schemas import LocationCreate, LocationTypeCreate, LocationUpdate

router = APIRouter(
    prefix="/admin_panel",
    tags=["admins"]
)


@router.get("/user_roles", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def get_users_amn_roles(  
    role: str | None = None,
    session: AsyncSession = Depends(get_session)
):
    return  await get_users_roles(session=session, role=role)


@router.post("/location_type", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def add_new_type(
    locatoin_type: LocationTypeCreate,
    session: AsyncSession = Depends(get_session)
):
    return await add_type(session=session, type_create=locatoin_type)
    

@router.post("/locatoin", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def add_new_location(
    new_location: LocationCreate,
    session: AsyncSession = Depends(get_session)
):
    return await add_location(session=session, location_create=new_location)


@router.put("/location/{location_id}", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def update_location(
    location_id: int,
    location_update: LocationUpdate,
    session: AsyncSession = Depends(get_session)
):
    return await update_location_by_id(session=session, location_id=location_id, location_update=location_update)


@router.delete("/location/{location_id}", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def delete_location(
    location_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await delete_locations_by_id(session=session, location_id=location_id)


@router.get("/review", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def get_review(
    review_id: int | None = None,
    session: AsyncSession = Depends(get_session)
):
    return await get_all_reviews(session=session, review_id=review_id)


@router.delete("/review", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def delete_review(
    review_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await delete_review_by_id(session=session, review_id=review_id)