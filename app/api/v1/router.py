from fastapi import APIRouter
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from app_services_parent.infinity.app.main import app as infinity_app
from app_services_parent.shipment.app.main import app as shipment_app
from app_services_parent.onboarding.app.main import app as onboarding_app
from app_services_parent.settlement.app.main import app as settlement_app
from app_services_parent.operations.app.main import app as operations_app
from app_services_parent.pre_onboarding.app.main import app as pre_onboarding_app
from .health import create_health_router
import logging

from dotenv import load_dotenv



env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../", "env", ".env"))
load_dotenv(env_path)

logger = logging.getLogger(__name__)

def create_v1_router() -> APIRouter:
    # Create base v1 router
    v1_router = APIRouter(prefix="/api/v1")

    # Add main health endpoint
    @v1_router.get("/health")
    async def main_health():
        return {
            "status": "healthy",
            "version": "1.0.0",
            "profile": os.getenv("PROFILE"),
            "services": {
                "shipment": {"port": 8080},
                "onboarding": {"port": 8080},
                "settlement": {"port": 8080},
                "operations": {"port": 8080},
                "pre_onboarding": {"port": 8080},
                "infinity": {"port": 8080}
            }
        }

    # Mount all service routes
    services = {
        'shipment': shipment_app,
        'onboarding': onboarding_app,
        'settlement': settlement_app,
        'operations': operations_app,
        'pre_onboarding': pre_onboarding_app,
        'infinity': infinity_app
    }

    for app in services.values():
        for route in app.routes:
            v1_router.routes.append(route)

    return v1_router