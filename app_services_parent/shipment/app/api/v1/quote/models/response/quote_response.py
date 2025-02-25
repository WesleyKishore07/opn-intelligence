from datetime import datetime
from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field

class ServiceOption(BaseModel):
    service_level: str = Field(..., description="Service level type")
    base_charge: Decimal = Field(..., description="Base shipping charge")
    fuel_surcharge: Decimal = Field(..., description="Fuel surcharge")
    total_charge: Decimal = Field(..., description="Total shipping charge")
    estimated_delivery: datetime = Field(..., description="Estimated delivery date and time")

class QuoteResponse(BaseModel):
    quote_id: str = Field(..., description="Unique quote identifier")
    service_options: List[ServiceOption] = Field(..., description="Available shipping options")
    created_at: datetime = Field(..., description="Quote creation timestamp")
    valid_until: datetime = Field(..., description="Quote validity timestamp")
    currency: str = Field("USD", description="Currency for all monetary values")