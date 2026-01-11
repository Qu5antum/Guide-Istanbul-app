from langchain.tools import tool
from backend.src.database.db import async_session
from backend.src.services.locations_service import get_location_by_category
from math import radians, sin, cos, sqrt, atan2


@tool
async def user_search_request_by_locationtype_and_distance(
    type_name: str,
    user_lat: float,
    user_lon: float
   ):
    """
    Use only if the user wants to find locations by their category, for example: museum, restaurant, historical sites, etc.
    Calculates distance in kilometers between user and a place.
    """

    async with async_session() as session:
        locations = await get_location_by_category(session=session, type_name=type_name)

    def calculate_distance(
        user_lat: float,
        user_lon: float,
        place_lat: float,
        place_lon: float
    ) -> float:
        R = 6371

        dlat = radians(place_lat - user_lat)
        dlon = radians(place_lon - user_lon)

        a = (
            sin(dlat / 2) ** 2 +
            cos(radians(user_lat)) *
            cos(radians(place_lat)) *
            sin(dlon / 2) ** 2
        )

        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return round(R * c, 2)
    
   
    return "\n\n".join(
        f"{loc.location_title}\n"
        f"Price: {loc.price or 'Free'}\n"
        f"Distance in km: {calculate_distance(user_lat=user_lat, user_lon=user_lon, place_lat=loc.latitude, place_lon=loc.longitude)}"
        for loc in locations[:5]
    )


