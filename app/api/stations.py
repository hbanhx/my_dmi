from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models.model import Station
from app.schemas.schema import StationBase, StationResponse



router = APIRouter(prefix="/items", tags=["Stations"])

# /v2/metObs/collections/station/items
@router.get("/", response_model=StationResponse)
def Get_stations(
    stationId: str | None = None,
    offset: int = 0, 
    limit: int = 1000,
    db: Session = Depends(get_db)
    ):
    stations = db.query(Station)

    if stationId:
        stations = stations.filter(Station.station_id == stationId)

    stations = stations.offset(offset).limit(limit).all()

    return {
        "numberReturned": len(stations),
        "offset": offset,
        "limit": limit,
        "stations": stations
    }


# /v2/metObs/collections/station/items/{id}
@router.get("/{id}", response_model=StationBase)
def get_station(
    id: str,
    db: Session = Depends(get_db)
    ):
    station = db.query(Station).filter(Station.feature_id == id).first()
    
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    
    return station