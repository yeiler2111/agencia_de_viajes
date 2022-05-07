
from xmlrpc.client import boolean
from sqlalchemy import column, integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.app import user
from database.session import Base
from enum import Enum
class User(Base):
    __tablename__="user"
    id = column(integer, primary_key=True, autoincrement = True)
    fullname = column(str(50))
    username=column(str(50))
    password= column(str(50))
    booking= relationship("Booking", back_populate="user" )   

class Booking(Base):
    __tablename__="booking"
    id = column(integer, primary_key=True, autoincrement = True)
    status = column(BookingStatus)
    outboundFlight= column(Flight)
    paymentToken= column(String(50)) 
    checkedIn= column(boolean) 
    customer= column(User) 
    createdAt= column(String(50)) 
    bookingReference= column(String(50)) 
    users=relationship("user")
    user=relationship("User", back_populate="bookings")
    flight=relationship("Flight", back_populate="")


class Flight(Base):
    __tablename__="flight"
    id = column(integer, primary_key=True, autoincrement = True)
    departuredate= column(String(50))
    departureAirportCode= column(String(50))
    departureAirportName= column(String(50))
    departureCity= column(String(50))
    departureLocale= column(String(50))
    arrivalDate= column(String(50))
    arrivalAirportCode= column(String(50))
    arrivalAirportName= column(String(50))
    arrivalCity= column(String(50))
    arrivalLocale= column(String(50))
    ticketPrice= column(integer)
    ticketCurrency= column(String(50))
    flightNumber= column(integer)
    seatCapacity= column(integer)
    bookings=relationship("Booking", back_populate="flight")
    
class bookingstatus(Enum):
    UNCONFIRMED=1
    CONFIRMED=2
    CANSELLED=3    
        

#class bookingstatus(Base):
    
        
    
    