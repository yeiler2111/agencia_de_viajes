from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi.responses import PlainTextResponse
from app.database import mydb
from . import schema
from . import services
from . import validation
from app.core import security
from app.user import schema as user_schema
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date


api_router = APIRouter(tags = ["Catalog"])


@api_router.get("/catalog/all", response_model = List[schema.Flight])
async def get_all_flights(mydb_session: Session = Depends(mydb.get_mydb_session)):
    return await services.get_all_flights(mydb_session)

@api_router.get("/catalog/", response_model=List[schema.Flight])
async def get_flights(departureAirportCode: str, arrivalAirportCode: str, departureDate: date, mydb_session: Session = Depends(mydb.get_mydb_session)):
    flights = await services.get_flights(departureAirportCode,arrivalAirportCode,departureDate,mydb_session)
    if not flights:
        raise HTTPException(status_code=404, detail="flight(s) not found")

    return flights

@api_router.get("/catalog/{airportCode}", response_model=List[schema.Flight])
async def get_flights_by_airportcode_and_departuredate(airportCode: str, departureDate: Optional[date] = None, mydb_session: Session = Depends(mydb.get_mydb_session)):
    flights = await services.get_flights_by_departureairportcode_and_departuredate(airportCode,departureDate,mydb_session)
    if not flights:
        raise HTTPException(status_code=404, detail="flight(s) not found")

    return flights

@api_router.post("/catalog/", status_code = status.HTTP_201_CREATED, response_model=schema.Flight)
async def create_flight(flight_in: schema.FlightCreate, mydb_session: Session = Depends(mydb.get_mydb_session),
                        current_user: user_schema.User = Depends(security.get_current_user)):
    new_flight = await services.create_new_flight(flight_in, mydb_session = mydb_session)
    return new_flight

@api_router.put('/catalog/{id}', status_code = status.HTTP_201_CREATED)
async def update_flight(id: int, flight: schema.FlightUpdate, mydb_session: Session = Depends(mydb.get_mydb_session),
                        current_user: user_schema.User = Depends(security.get_current_user)):
    existingflight = await validation.verify_flight_exist(id, mydb_session)
    if not existingflight:
        raise HTTPException(status_code=404, detail="Non-existent flight")
    
    new_flight = await services.update_flight(id, flight, mydb_session)
    return new_flight

@api_router.delete("/catalog/{id}", status_code=status.HTTP_200_OK, response_class=PlainTextResponse)
async def delete_flight(id: int, mydb_session: Session = Depends(mydb.get_mydb_session),
                        current_user: user_schema.User = Depends(security.get_current_user)):
    existingflight = await validation.verify_flight_exist(id, mydb_session)
    if not existingflight:
        raise HTTPException(status_code=404, detail="Non-existent flight")
    await services.delete_flight(id, mydb_session)

    return "THE FLIGHT AND ALL HIS BOOKINGS HAVE BEEN SUCCESSFULLY DELETED."