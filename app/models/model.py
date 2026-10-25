from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

# ORM representation af database atbeller

class Station(Base):
    __tablename__ = "stations"
    __table_args__ = {"schema": "dmi"}

    station_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    feature_id = Column(String, unique=True)

    observations = relationship("Observation", back_populates="station") # sqlalchemy ORM relation


class Observation(Base):
    __tablename__ = "observations"
    __table_args__ = {"schema": "dmi"}

    id = Column(Integer, primary_key=True)
    feature_id = Column(String, unique=True)
    station_id = Column(String, ForeignKey("dmi.stations.station_id"), nullable=False)
    parameter_id = Column(String)
    observed = Column(DateTime) 
    value = Column(Float)  
    created_at = Column(DateTime) 

    station = relationship("Station", back_populates="observations") # sqlalchemy ORM relation