import pytest
from fastapi import status
from unittest.mock import patch

class TestQuoteController:
    def test_calculate_quote_success(self, client, quote_api_url, valid_quote_request):
        response = client.post(f"{quote_api_url}/calculate", json=valid_quote_request)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert "quote_id" in data
        assert "service_options" in data
        assert len(data["service_options"]) == 1
        assert "created_at" in data
        assert "valid_until" in data
        assert data["currency"] == "USD"

    def test_calculate_quote_invalid_service_level(self, client, quote_api_url, valid_quote_request):
        request_with_invalid_service = valid_quote_request.copy()
        request_with_invalid_service["service_level"] = "invalid_level"
        response = client.post(f"{quote_api_url}/calculate", json=request_with_invalid_service)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_calculate_quote_invalid_package(self, client, quote_api_url, valid_quote_request):
        request_with_invalid_package = valid_quote_request.copy()
        request_with_invalid_package["packages"][0]["weight"] = -1
        response = client.post(f"{quote_api_url}/calculate", json=request_with_invalid_package)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_calculate_quote_missing_service_level(self, client, quote_api_url, valid_quote_request):
        request_without_service = valid_quote_request.copy()
        del request_without_service["service_level"]
        response = client.post(f"{quote_api_url}/calculate", json=request_without_service)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @pytest.mark.asyncio
    async def test_calculate_quote_service_error(self, client, quote_api_url, valid_quote_request):
        with patch('app.api.v1.quote.services.quote_service.QuoteService.calculate_quote') as mock_calculate:
            mock_calculate.side_effect = Exception("Service calculation error")
            response = client.post(f"{quote_api_url}/calculate", json=valid_quote_request)
            assert response.status_code == status.HTTP_400_BAD_REQUEST