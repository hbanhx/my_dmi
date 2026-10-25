from pydantic import BaseModel
from datetime import datetime
from typing import List

# pydantic models: lib for data validation, 
# schema for request/response validation

class StationBase(BaseModel):
    station_id: str
    name: str
    feature_id: str

class ObservationBase(BaseModel):
    feature_id: str
    station_id: str
    parameter_id: str
    observed: datetime
    value: float
    created_at: datetime


class StationResponse(BaseModel):
    numberReturned: int
    offset: int
    limit: int
    stations: List[StationBase]


class ObservationResponse(BaseModel):
    numberReturned: int
    offset: int
    limit: int
    observations: List[ObservationBase]