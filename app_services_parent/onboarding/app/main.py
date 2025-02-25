# app-services-parent/onboarding/app/main.py
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from common.config.base_config import get_service_port
import os

SERVICE_NAME = "onboarding"

def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Create API router with full path prefix
    api_router = APIRouter(prefix="/api/v1/onboarding")

    @api_router.get("/health")
    async def health_check():
        return {
            "service": SERVICE_NAME,
            "status": "healthy",
            "version": "1.0.0",
            "environment": os.getenv("ENVIRONMENT", "development"),
            "port": get_service_port(SERVICE_NAME)
        }

    # Include the API router
    app.include_router(api_router)

    return app

app = create_app()