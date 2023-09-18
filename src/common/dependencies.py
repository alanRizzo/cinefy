from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.settings import settings


@lru_cache(maxsize=None)
def get_db_url_no_driver() -> str:
    db_username = settings.DB_USERNAME
    db_pass = settings.DB_PASSWORD
    db_host = settings.DB_HOST
    db_port = settings.DB_PORT
    db_name = settings.DB_NAME
    return f"{db_username}:{db_pass}@{db_host}:{db_port}/{db_name}"


def get_db_sync_url() -> str:
    driver = "postgresql+psycopg2"
    db_connection = get_db_url_no_driver()
    return f"{driver}://{db_connection}"


engine = create_engine(get_db_sync_url(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    try:
        with SessionLocal() as db_session:
            yield db_session
            db_session.commit()
    except Exception as err:
        db_session.rollback()
        logger.error(err)
    finally:
        db_session.close()


SessionDep = Annotated[Session, Depends(get_db)]
