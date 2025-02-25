from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field

class Address(BaseModel):
    street: str = Field(
        ...,
        min_length=1,
        description="Street address",
        json_schema_extra={"example": "123 Main St"}
    )
    city: str = Field(
        ...,
        min_length=1,
        description="City name",
        json_schema_extra={"example": "New York"}
    )
    state: str = Field(
        ...,
        min_length=1,
        description="State code",
        json_schema_extra={"example": "NY"}
    )
    country: str = Field(
        ...,
        min_length=1,
        description="Country code",
        json_schema_extra={"example": "USA"}
    )
    postal_code: str = Field(
        ...,
        min_length=1,
        description="Postal code",
        json_schema_extra={"example": "10001"}
    )

class Package(BaseModel):
    weight: Decimal = Field(
        ...,
        gt=0,
        description="Package weight in kg",
        json_schema_extra={"example": 10.5}
    )
    length: Decimal = Field(
        ...,
        gt=0,
        description="Package length in cm",
        json_schema_extra={"example": 20.0}
    )
    width: Decimal = Field(
        ...,
        gt=0,
        description="Package width in cm",
        json_schema_extra={"example": 15.0}
    )
    height: Decimal = Field(
        ...,
        gt=0,
        description="Package height in cm",
        json_schema_extra={"example": 12.0}
    )
    description: Optional[str] = Field(
        None,
        description="Package contents description",
        json_schema_extra={"example": "Electronics"}
    )