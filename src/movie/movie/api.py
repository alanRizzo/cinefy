from fastapi import APIRouter, Depends, HTTPException, status

from src.movie.schemas import MovieInput, MovieOutput
from src.movie.services import MovieService

api = APIRouter()


@api.post("/movie", response_model=None)
def create_movie(movie_data: MovieInput, service: MovieService = Depends()):
    service.create_movie(movie_data.dict())


@api.get("/movie/{movie_id}", response_model=MovieOutput)
def get_movie(movie_id: int, service: MovieService = Depends()):
    if movie := service.get_movie(movie_id):
        return movie
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")


@api.get("/movie", response_model=list[MovieOutput])
def get_all_movies(service: MovieService = Depends()):
    return service.get_all_movies()


@api.put("/movie/{movie_id}", response_model=None)
def update_movie(
    movie_id: int, updated_data: MovieInput, service: MovieService = Depends()
):
    if not service.get_movie(movie_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    service.update_movie(movie_id, updated_data.dict())


@api.delete("/movie/{movie_id}", response_model=None)
def delete_movie(movie_id: int, service: MovieService = Depends()):
    if not service.get_movie(movie_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found"
        )
    service.delete_movie(movie_id)
