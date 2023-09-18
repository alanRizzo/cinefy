from pydantic import BaseModel

from src.seat.schemas import SeatRead


class RoomCreate(BaseModel):
    name: str
    theatre_id: int


class RoomRead(BaseModel):
    id: int
    name: str
    theatre_id: int
    seats: list[SeatRead] = []
