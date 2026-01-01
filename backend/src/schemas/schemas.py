from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import List

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponce(BaseModel):
    id: int
    username: str
    email: EmailStr
    roles: List[str]

    class Config:
        from_attributes = True 


class LocationCreate(BaseModel):
    location_title: str
    description: str
    price: str | None = None
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    adres: str
    link: HttpUrl | None = None
    type_ids: List[int]


class LocationResponce(BaseModel):
    id: int
    location_title: str
    latitude: float
    longitude: float
    adres: str
    link: HttpUrl | None

    class Config:
        from_attributes = True


class LocationTypeCreate(BaseModel):
    name: str

class LocationTypeResponce(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True