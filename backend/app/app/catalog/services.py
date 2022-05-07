from typing import List, Optional
from sqlalchemy.orm import Session
from . import models
from . import schema
from app.user import models as user_models
from fastapi import HTTPException


async def get_booking_by_id(booking_id: int, mydb_session: Session) -> models.Booking:
    booking_info = mydb_session.query(models.Booking).get(booking_id)
    return booking_info

async def get_bookings_by_idflight(flight_id: int, mydb_session: Session) -> List[models.Booking]:
    bookings = mydb_session.query(models.Booking).filter(models.Booking.outboundFlight_id == flight_id).all()
    return bookings

async def get_bookings_by_status_and_customername(status: schema.BookingStatus, customername: str, mydb_session: Session) -> List[models.Booking]:
    if status and customername:
        user = mydb_session.query(user_models.User).filter(user_models.User.fullname == customername).first()
        bookings = mydb_session.query(models.Booking).filter(models.Booking.status == status, 
                                                           models.Booking.customer_id == user.id).all()
    elif not status and customername:
        user = mydb_session.query(user_models.User).filter(user_models.User.fullname == customername).first()
        bookings = mydb_session.query(models.Booking).filter(models.Booking.customer_id == user.id).all()
    elif status and not customername:
        bookings = mydb_session.query(models.Booking).filter(models.Booking.status == status).all()
    else:
        bookings = mydb_session.query(models.Booking).all()
    return bookings

async def create_new_booking(flight_id: int, user_id: int, booking: schema.BookingCreate, mydb_session: Session) -> models.Booking:
    new_booking = models.Booking(outboundFlight_id=flight_id,
                                 customer_id=user_id,
                                 **booking.dict())
    mydb_session.add(new_booking)
    mydb_session.commit()
    mydb_session.refresh(new_booking)
    return new_booking

async def delete_booking_by_id(booking_id: int, mydb_session: Session):
    mydb_session.query(models.Booking).filter(models.Booking.id == booking_id).delete()
    mydb_session.commit()