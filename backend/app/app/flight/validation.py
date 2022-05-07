from typing import Optional
from sqlalchemy.orm import Session
from . import models

async def verify_flight_exist(flight_id: int, mydb_session: Session) -> Optional[models.Flight]:
    return mydb_session.query(models.Flight).filter(models.Flight.id == flight_id).first()