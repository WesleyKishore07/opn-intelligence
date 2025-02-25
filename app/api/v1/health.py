from fastapi import APIRouter
from typing import Dict
from common.config.base_config import get_service_port

def create_health_router(service_info: Dict[str, Dict]) -> APIRouter:
    router = APIRouter()

    @router.get("/health", tags=["health"])
    async def health_check() -> Dict:
        return {
            "status": "healthy",
            "version": "1.0.0",
            "monolith_port": 8080,
            "services": {
                service: {
                    "status": "healthy",
                    "configured_port": info["port"],
                    "currently_running_on": 8080
                }
                for service, info in service_info.items()
            }
        }
    return router