from contextlib import asynccontextmanager

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.health_check.api import api as health_check_api
from src.movie.api import api as movie_api
from src.settings import settings

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI()


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


def create_app() -> FastAPI:
    base_app = FastAPI(
        title="Cinefy",
        lifespan=lifespan,
    )
    base_app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_headers=["*"],
        allow_methods=["*"],
    )
    base_app.include_router(health_check_api, tags=["HealthCheck"])
    base_app.include_router(movie_api, tags=["Movie"])
    return base_app


app = create_app()
