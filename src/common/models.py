from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    release_date = Column(Date)
    genre = Column(String(100))
    director = Column(String(100))
    description = Column(Text)

    def __init__(self, title, release_date, genre, director, description):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.director = director
        self.description = description

    def __repr__(self):
        return (
            f"<Movie(id={self.id}, title='{self.title}', director='{self.director}')>"
        )


class Theatre(Base):
    __tablename__ = "theatres"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    location = Column(String(255))

    rooms = relationship("Room", back_populates="theatre")

    def __init__(self, name, location):
        self.name = name
        self.location = location


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    theatre_id = Column(Integer, ForeignKey("theatres.id"))

    theatre = relationship("Theatre", back_populates="rooms")
    seats = relationship("Seat", back_populates="room")

    def __init__(self, name, theatre_id):
        self.name = name
        self.theatre_id = theatre_id


class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    row = Column(String(5), nullable=False)
    number = Column(Integer, nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"))

    room = relationship("Room", back_populates="seats")

    def __init__(self, row, number, room_id):
        self.row = row
        self.number = number
        self.room_id = room_id
