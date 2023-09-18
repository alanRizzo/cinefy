from fastapi import APIRouter, Depends

from src.health_check.schemas import HealthCheck
from src.health_check.services import HealthCheckService

api = APIRouter()


@api.get("/health")
def get_health_check(service: HealthCheckService = Depends()) -> HealthCheck:
    return service.okay()
