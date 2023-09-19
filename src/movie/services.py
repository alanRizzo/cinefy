from sqlalchemy.orm import Session

from src.common.models import Movie
from src.movie.schemas import MovieCreate


class MovieService:
    """Store the entities in our domain model.

    The signatures of these methods consist of domain models and query parameters to
    filter or paginate the response.
    They do not expose how they persist entities, only which entities they persist.
    """

    @staticmethod
    def create_movie(db: Session, movie_data: MovieCreate):
        """Create a new movie record in the database."""
        db.add(Movie(**movie_data.model_dump()))

    @staticmethod
    def get_movie(db: Session, movie_id: int):
        """Retrieve a movie record by its ID."""
        return db.query(Movie).filter_by(id=movie_id).first()

    @staticmethod
    def get_all_movies(db: Session):
        """Retrieve all movie records from the database."""
        return db.query(Movie).all()

    @staticmethod
    def update_movie(db: Session, movie_id: int, updated_data: MovieCreate):
        """Update a movie record with new data."""
        if movie := db.query(Movie).filter_by(id=movie_id).first():
            for key, value in updated_data.dict().items():
                setattr(movie, key, value)

    @staticmethod
    def delete_movie(db: Session, movie_id: int):
        if movie := db.query(Movie).filter_by(id=movie_id).first():
            db.delete(movie)
