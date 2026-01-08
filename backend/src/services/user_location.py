import httpx

async def get_location_from_ip(ip: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"https://ipinfo.io/{ip}/json")
        data = res.json()

    city = data.get("city")
    loc = data.get("loc")

    if loc:
        lat, lon = loc.split(",")
        return {
            "city": city,
            "latitude": float(lat),
            "longitude": float(lon)
        }

    return None

    #ip = request.client.host
