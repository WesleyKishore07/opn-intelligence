import os
import sys
from pathlib import Path
import pytest
import asyncio

# Fix the ROOT_DIR to the correct location
ROOT_DIR = Path(__file__).resolve().parent  # This points to /home/runner/work/opn-intelligence/opn-intelligence

def pytest_sessionstart(session):
    """
    Called after the Session object has been created and before performing collection
    and entering the run test loop.
    """
    app_services_path = ROOT_DIR / 'app_services_parent'
    
    if not app_services_path.exists():
        raise FileNotFoundError(f"Expected directory not found: {app_services_path}")

    # Add each service directory to Python path
    for service_dir in app_services_path.iterdir():
        if service_dir.is_dir() and not service_dir.name.startswith('.'):
            service_path = str(service_dir)
            if service_path not in sys.path:
                sys.path.insert(0, service_path)

    # Set environment variables for testing
    os.environ.setdefault('DEPLOYMENT_MODE', 'monolith')
    os.environ.setdefault('SERVICE_NAME', 'shipment')

def pytest_configure(config):
    """Configure pytest"""
    # Add asyncio marker
    config.addinivalue_line(
        "markers",
        "asyncio: mark test as an async test"
    )

    # Configure asyncio mode
    config.option.asyncio_mode = "auto"

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
def anyio_backend():
    """Configure backend for anyio."""
    return "asyncio"
