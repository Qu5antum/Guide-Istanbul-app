import math
from langchain.tools import tool


@tool
async def calculate_distance(
    user_lat: float,
    user_lng: float,
    place_lat: float,
    place_lng: float
) -> float:
    """
    Сalculate the distance from the user to the location
    """
    R = 6371 
    lat1, lon1, lat2, lon2 = map(
        math.radians,
        [user_lat, user_lng, place_lat, place_lng]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c, 2)
