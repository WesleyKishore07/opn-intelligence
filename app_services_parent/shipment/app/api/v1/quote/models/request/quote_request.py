from typing import List
from pydantic import BaseModel, Field
from ..entities.quote import Address, Package

class QuoteRequest(BaseModel):
    origin: Address
    destination: Address
    packages: List[Package] = Field(..., min_items=1)
    service_level: str = Field(
        ...,
        description="Shipping service level",
        pattern="^(standard|express|priority)$"
    )