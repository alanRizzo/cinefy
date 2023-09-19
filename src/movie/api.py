from fastapi import APIRouter

from src.common.dependencies import SessionDep
from src.common.exceptions import MOVIE_NOT_FOUND
from src.movie.schemas import MovieCreate, MovieRead
from src.movie.services import MovieService

api = APIRouter()


@api.post("/movie", response_model=None)
def create_movie(movie_data: MovieCreate, db: SessionDep):
    return MovieService.create_movie(db, movie_data)


@api.get("/movie/{movie_id}", response_model=MovieRead)
def get_movie(movie_id: int, db: SessionDep):
    if movie := MovieService.get_movie(db, movie_id):
        return movie
    raise MOVIE_NOT_FOUND


@api.get("/movie", response_model=list[MovieRead])
def get_all_movies(db: SessionDep):
    return MovieService.get_all_movies(db)


@api.put("/movie/{movie_id}", response_model=None)
def update_movie(movie_id: int, updated_data: MovieCreate, db: SessionDep):
    if not MovieService.get_movie(db, movie_id):
        raise MOVIE_NOT_FOUND
    MovieService.update_movie(db, movie_id, updated_data)


@api.delete("/movie/{movie_id}", response_model=None)
def delete_movie(movie_id: int, db: SessionDep):
    if not MovieService.get_movie(db, movie_id):
        raise MOVIE_NOT_FOUND
    MovieService.delete_movie(db, movie_id)
