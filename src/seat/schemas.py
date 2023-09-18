from pydantic import BaseModel


class SeatCreate(BaseModel):
    row: str
    number: int
    room_id: int


class SeatRead(BaseModel):
    id: int
    row: str
    number: int
    room_id: int
