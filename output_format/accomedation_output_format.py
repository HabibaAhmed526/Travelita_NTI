from pydantic import BaseModel, Field
from typing import List, Dict, Optional


# Define a model for the hotel details
class Hotel(BaseModel):
    name: str = Field(..., title="Hotel Name")
    description: str = Field(..., title="Hotel Description")
    price: float = Field(..., title="Hotel Price")
    rating: float = Field(..., title="Hotel Rating", ge=0, le=5)
    address: str = Field(..., title="Hotel Address")
    link: str = Field(..., title="Hotel Link")

# Define a model for the list of hotels
class HotelList(BaseModel):
    hotel_names: List[Hotel] = Field(..., title="List of Hotels")