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
    price: float | None = Field(None, ge=0)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    link: HttpUrl | None = None
    type_id: List[int]


class LocationResponce(BaseModel):
    id: int
    location_title: str
    latitude: float
    longitude: float
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