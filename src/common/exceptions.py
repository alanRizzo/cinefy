from fastapi import HTTPException, status

MOVIE_NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Movie not found",
)
