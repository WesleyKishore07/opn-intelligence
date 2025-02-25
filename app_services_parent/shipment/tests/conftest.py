import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add shipment service root to Python path
shipment_root = Path(__file__).parent.parent
if str(shipment_root) not in sys.path:
    sys.path.insert(0, str(shipment_root))

from app.main import create_app

@pytest.fixture(scope="session")
def app():
    """Create test app instance"""
    return create_app()

@pytest.fixture(scope="session")
def client(app):
    """Create test client"""
    return TestClient(app)

@pytest.fixture
def base_api_url():
    """Base API URL for all endpoints"""
    return "/api/v1/shipment"