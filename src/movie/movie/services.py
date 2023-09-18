from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.common.models import Movie


class MovieService:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_movie(self, movie_data):
        """Create a new movie record in the database."""
        session = self.Session()
        movie = Movie(**movie_data)
        session.add(movie)
        session.commit()
        session.close()

    def get_movie(self, movie_id):
        """Retrieve a movie record by its ID."""
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        session.close()
        return movie

    def get_all_movies(self):
        """Retrieve all movie records from the database."""
        session = self.Session()
        movies = session.query(Movie).all()
        session.close()
        return movies

    def update_movie(self, movie_id, updated_data):
        """Update a movie record with new data."""
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        if movie:
            for key, value in updated_data.items():
                setattr(movie, key, value)
            session.commit()
        session.close()

    def delete_movie(self, movie_id):
        """Delete a movie record by its ID."""
        session = self.Session()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        if movie:
            session.delete(movie)
            session.commit()
        session.close()
