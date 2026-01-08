from langchain.tools import tool
from backend.src.database.db import async_session
from backend.src.services.locations_service import get_location_by_category
import json



@tool
async def user_search_request_by_locationtype(type_name: str):
    """
    Use only if the user wants to find locations by their category, for example: museum, restaurant, historical sites, etc.
    """

    async with async_session() as session:
        locations = await get_location_by_category(session=session, type_name=type_name)
   
    return "\n\n".join(
        f"{loc.location_title}\n"
        f"Price: {loc.price or 'Free'}\n"
        f"Coordinates: {loc.latitude}, {loc.longitude}"
        for loc in locations[:5]
    )


