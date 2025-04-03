from fastapi import APIRouter, Depends
from app.core.services import SystemService
from app.core.models import SystemStatus

router = APIRouter(
    prefix="/system",
    tags=["system"]
)

# Simple dependency to get the service
def get_system_service() -> SystemService:
    return SystemService()

@router.get("/health", response_model=SystemStatus, tags=["system"])
def health_check(
    system_service: SystemService = Depends(get_system_service)
) -> SystemStatus:
    return system_service.check_system_status()