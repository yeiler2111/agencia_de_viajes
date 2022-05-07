from typing import Optional
from . import models
from sqlalchemy.orm import Session

async def verify_bookingreference_exist(bookingreference: str, mydb_session: Session) -> Optional[models.User]:
    return mydb_session.query(models.Booking).filter(models.Booking.bookingReference == bookingreference).first()