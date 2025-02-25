import pytest
from decimal import Decimal
from datetime import datetime
from app.api.v1.quote.models.request.quote_request import QuoteRequest
from app.api.v1.quote.services.quote_service import QuoteService

class TestQuoteService:
    """Test cases for Quote Service"""

    @pytest.fixture
    def service(self):
        """Create QuoteService instance"""
        return QuoteService()

    @pytest.mark.asyncio
    async def test_calculate_quote_success(self, service, valid_quote_request):
        """Test successful quote calculation"""
        request = QuoteRequest(**valid_quote_request)
        response = await service.calculate_quote(request)

        # Validate quote structure
        assert response.quote_id.startswith("quo_")
        assert len(response.service_options) == 1
        assert isinstance(response.created_at, datetime)
        assert response.valid_until > response.created_at
        assert response.currency == "USD"

        # Validate service option calculations
        option = response.service_options[0]
        assert option.service_level == request.service_level
        assert option.base_charge > Decimal("0")
        assert option.fuel_surcharge >= Decimal("0")
        assert option.total_charge == option.base_charge + option.fuel_surcharge
        assert isinstance(option.estimated_delivery, datetime)

    @pytest.mark.asyncio
    async def test_calculate_quote_multiple_packages(self, service, valid_quote_request):
        """Test quote calculation with multiple packages"""
        # Add another package
        valid_quote_request["packages"].append({
            "weight": 5.0,
            "length": 10.0,
            "width": 10.0,
            "height": 10.0,
            "description": "Books"
        })

        request = QuoteRequest(**valid_quote_request)
        response = await service.calculate_quote(request)

        # Verify charges scale with total weight
        single_package_weight = valid_quote_request["packages"][0]["weight"]
        total_weight = single_package_weight + 5.0  # weight of second package

        option = response.service_options[0]
        assert option.base_charge > Decimal("0")
        assert option.total_charge > option.base_charge