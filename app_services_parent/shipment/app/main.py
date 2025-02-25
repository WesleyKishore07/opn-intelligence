# app_services_parent/shipment/app/main.py
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.quote.controllers import router as quote_router
from common.config.base_config import get_service_port
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def create_app() -> FastAPI:
    logger.debug("Creating shipment app...")
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    router = APIRouter()

    @router.get("/api/v1/shipment/health")
    async def health_check():
        logger.debug("Health check called")
        return {
            "service": "shipment",
            "status": "healthy",
            "version": "1.0.0",
            "environment": os.getenv("ENVIRONMENT", "development"),
            "port": get_service_port("shipment")
        }

    app.include_router(router)
    app.include_router(quote_router, prefix="/api/v1/shipment")

    logger.debug("Shipment app routes:")
    for route in app.routes:
        logger.debug(f"Registered route: {route.methods} {route.path}")

    return app

app = create_app()