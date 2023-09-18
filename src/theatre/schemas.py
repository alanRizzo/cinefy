from pydantic import BaseModel

from src.room.schemas import RoomCreate


class TheatreCreate(BaseModel):
    name: str
    location: str


class TheatreRead(BaseModel):
    id: int
    name: str
    location: str
    rooms: list[RoomCreate] = []
