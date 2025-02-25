import pytest
from pydantic import ValidationError
from app.api.v1.quote.models.entities.quote import Address, Package

class TestQuoteModels:
    """Test cases for Quote related models"""

    def test_address_model_validation(self):
        """Test Address model validation"""
        # Test valid address
        valid_address = Address(
            street="123 Main St",
            city="New York",
            state="NY",
            country="USA",
            postal_code="10001"
        )
        assert valid_address.street == "123 Main St"
        assert valid_address.postal_code == "10001"

        # Test invalid cases
        invalid_cases = [
            # Empty street
            {
                "street": "",
                "city": "New York",
                "state": "NY",
                "country": "USA",
                "postal_code": "10001"
            },
            # Missing postal_code
            {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY",
                "country": "USA"
            },
            # Empty city
            {
                "street": "123 Main St",
                "city": "",
                "state": "NY",
                "country": "USA",
                "postal_code": "10001"
            }
        ]

        for invalid_case in invalid_cases:
            with pytest.raises(ValidationError):
                Address(**invalid_case)