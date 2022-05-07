from fastapi import APIRouter, Depends, status, Response, HTTPException
from app.user import validation as user_validation, services as user_services , schema as user_schema
from app.catalog import validation as catalog_validation
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import mydb
from . import schema
from . import services
from . import validation
from app.core import security

api_router = APIRouter(tags = ["Booking"])

@api_router.get('/booking/{id}', response_model = schema.Booking)
async def get_booking_by_id(id: int, mydb_session: Session = Depends(mydbget_mydb_session)):
    booking_info = await services.get_booking_by_id(id, mydb_session)
    if not booking_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking(s) not found")

    return booking_info

@api_router.get('/booking/flight/{idflight}', response_model = List[schema.Booking])
async def get_bookings_by_idflight(idflight: int, mydb_session: Session = Depends(mydbget_mydb_session)):
    existingflight = await catalog_validation.verify_flight_exist(idflight, mydb_session)
    if not existingflight:
        raise HTTPException(status_code=404, detail="Non-existent flight")
    
    bookings = await services.get_bookings_by_idflight(idflight, mydb_session)
    if not bookings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking(s) not found")

    return bookings

@api_router.get('/booking/', response_model = List[schema.Booking])
async def get_bookings_by_status_and_customername(status: Optional[schema.BookingStatus] = None, customername: Optional[str] = None, mydb_session: Session = Depends(mydbget_mydb_session)):
    if customername:
        existinguser = await user_validation.verify_fullname_exist(customername, mydb_session)
        if not existinguser:
            raise HTTPException(status_code=404, detail = "Non-existent user")
    bookings = await services.get_bookings_by_status_and_customername(status,customername, mydb_session)
    if not bookings:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Booking(s) not found")

    return bookings

@api_router.post("/booking/flight/{idflight}/user/{iduser}", status_code = status.HTTP_201_CREATED, response_model=schema.Booking)
async def create_booking(idflight: int, iduser: int, booking_in: schema.BookingCreate, mydb_session: Session = Depends(mydbget_mydb_session),
                         current_user: user_schema.User = Depends(security.get_current_user)):
    existingflight = await catalog_validation.verify_flight_exist(idflight, mydb_session)
    if not existingflight:
        raise HTTPException(status_code=404, detail="Non-existent flight")
    
    existinguser = await user_services.get_user_by_id(iduser, mydb_session)
    if not existinguser:
        raise HTTPException(status_code=404, detail = "Non-existent user")

    existingreference = await validation.verify_bookingreference_exist(booking_in.bookingReference, mydb_session)
    if existingreference:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The booking with this reference already exists in the system.")

    new_booking = await services.create_new_booking(idflight, iduser, booking_in, mydb_session)
    return new_booking

@api_router.delete("/booking/{id}", status_code=status.HTTP_204_NO_CONTENT, response_class=PlainTextResponse)
async def delete_booking(id: int, mydb_session: Session = Depends(mydbget_mydb_session),
                         current_user: user_schema.User = Depends(security.get_current_user)):
    existingbooking = await services.get_booking_by_id(id, mydb_session)
    if not existingbooking:
        raise HTTPException(status_code=404, detail="Non-existent booking")
    deleted_booking = await services.delete_booking_by_id(id, mydb_session)
    return "The booking has been successfully deleted."