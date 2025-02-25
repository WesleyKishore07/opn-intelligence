# app_services_parent/shipment/app/api/v1/quote/controllers/quote_controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from ..services.quote_service import QuoteService
from ..models.request.quote_request import QuoteRequest
from ..models.response.quote_response import QuoteResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/quote",  # Keep it simple, the main router will add prefixes
    tags=["quote"]
)

@router.post("/calculate",
             response_model=QuoteResponse,
             status_code=status.HTTP_200_OK,
             description="Calculate shipping quote")
async def calculate_quote(
        request: QuoteRequest,
        quote_service: QuoteService = Depends(QuoteService)
) -> QuoteResponse:
    logger.info(f"Processing quote calculation request")
    try:
        return await quote_service.calculate_quote(request)
    except Exception as e:
        logger.error(f"Quote calculation error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )