import pytest
from decimal import Decimal

@pytest.fixture
def valid_quote_request():
    """
    Valid quote request fixture for quote-related tests
    """
    return {
        "origin": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "country": "USA",
            "postal_code": "10001"
        },
        "destination": {
            "street": "456 Market St",
            "city": "Los Angeles",
            "state": "CA",
            "country": "USA",
            "postal_code": "90007"
        },
        "packages": [
            {
                "weight": 10.5,
                "length": 20.0,
                "width": 15.0,
                "height": 12.0,
                "description": "Electronics"
            }
        ],
        "service_level": "express"
    }

@pytest.fixture
def quote_api_url(base_api_url):
    """
    Quote-specific API URL
    """
    return f"{base_api_url}/quote"