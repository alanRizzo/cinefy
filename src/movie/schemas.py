from datetime import date

from pydantic import BaseModel


class MovieCreate(BaseModel):
    title: str
    release_date: date
    genre: str
    director: str
    description: str


class MovieRead(BaseModel):
    id: int
    title: str
    release_date: date
    genre: str
    director: str
    description: str
