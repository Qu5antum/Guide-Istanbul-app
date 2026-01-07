from pydantic import BaseModel, EmailStr, HttpUrl, Field, field_validator
from typing import List
from datetime import timezone

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


class LocationUpdate(BaseModel):
    location_title: str | None = None
    description: str | None = None
    price: str | None = None
    latitude: float | None = Field(None, ge=-90, le=90)
    longitude: float | None = Field(None, ge=-180, le=180)
    adres: str | None = None
    link: HttpUrl | None = None
    type_ids: List[int] | None = None


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


class ReviewCreate(BaseModel):
    text: str = Field(min_length=3)
    rating: int = Field(ge=1, le=5)
    user_id: int
    location_id: int

    @field_validator("text")
    @classmethod
    def check_for_bad_words(cls, text):
        bad_words = ['fuck', 'asshole', 'dickhead', 'bitch', 'dumbass', 'ass', 'bastard', 'dick']

        if any(word in text.lower() for word in bad_words):
            raise ValueError("Ваш комментарий содержит недопустимые слова.")

        return text
    
class ReviewUpdate(BaseModel):
    text: str = Field(min_length=3)
    rating: int | None = Field(None, ge=1, le=5)

    @field_validator("text")
    @classmethod
    def check_for_bad_words(cls, text):
        bad_words = ['fuck', 'asshole', 'dickhead', 'bitch', 'dumbass', 'ass', 'bastard', 'dick']

        if any(word in text.lower() for word in bad_words):
            raise ValueError("Ваш комментарий содержит недопустимые слова.")

        return text
    

class AiMessagesCreate(BaseModel):
    prompt: str
    ai_message: str
    user_id: int





