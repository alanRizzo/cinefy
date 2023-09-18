from datetime import date

from pydantic import BaseModel


class MovieInput(BaseModel):
    title: str
    release_date: date
    genre: str
    director: str
    description: str


class MovieOutput(MovieInput):
    id: int
