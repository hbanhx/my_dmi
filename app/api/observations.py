from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.models.model import Observation
from app.schemas.schema import ObservationBase, ObservationResponse

router = APIRouter(prefix="/items", tags=["Observations"])


# /v2/metObs/collections/observation/items
@router.get("/", response_model=ObservationResponse) # Response with numberReturned and List[ObservationBase] = convert sql to FastAPI/Pydantic (JSON‑skabelon)
def get_observations(
    stationId: str | None = None,
    parameterId: str | None = None,
    offset: int = 0, 
    limit: int = 1000, 
    db: Session = Depends(get_db)
    ):

    # SQLAlchemy db_session .query() return query object 
    observations = db.query(Observation)

    if stationId:
        observations = observations.filter(Observation.station_id == stationId)

    if parameterId:
        observations = observations.filter(Observation.parameter_id == parameterId)

    
    observations: List[ObservationBase] = observations.offset(offset).limit(limit).all() # .all() returns list

    return {
        "numberReturned": len(observations),
        "offset": offset,
        "limit": limit,
        "observations": observations
    }


# /v2/metObs/collections/observation/items/{id}
@router.get("/{id}", response_model=ObservationBase)
def get_observation(
    id: str, 
    db: Session = Depends(get_db)
    ):
    observation = db.query(Observation).filter(
        Observation.feature_id == id).first()
    
    if not observation:
        raise HTTPException(status_code=404, detail="Observation not found")
    
    return observation