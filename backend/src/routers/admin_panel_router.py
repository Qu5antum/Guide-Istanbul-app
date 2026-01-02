from fastapi import APIRouter, Depends, status
from backend.src.dependencies.check_role import require_roles
from backend.src.admin_services.user_role import get_users_roles
from backend.src.admin_services.location_service import add_type, add_location, get_types, update_location_by_id, delete_locations_by_id
from backend.src.database.db import AsyncSession, get_session
from backend.src.schemas.schemas import LocationCreate, LocationTypeCreate, LocationUpdate

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


@router.get("/location_type/{type_id}", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def get_location_types(
    session: AsyncSession = Depends(get_session)
):
    return await get_types(session=session)
    

@router.post("/locatoins", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def add_new_location(
    new_location: LocationCreate,
    session: AsyncSession = Depends(get_session)
):
    return await add_location(session=session, location_create=new_location)


@router.put("/locations/{location_id}", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def update_location(
    location_id: int,
    location_update: LocationUpdate,
    session: AsyncSession = Depends(get_session)
):
    return await update_location_by_id(session=session, location_id=location_id, location_update=location_update)


@router.delete("/locations/{location_id}", dependencies=[Depends(require_roles(["admin"]))], status_code=status.HTTP_200_OK)
async def delete_location(
    location_id: int,
    session: AsyncSession = Depends(get_session)
):
    return await delete_locations_by_id(session=session, location_id=location_id)