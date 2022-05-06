from datetime import date
import string
from xmlrpc.client import boolean
from sqlalchemy import column, integer, String, Boolean
from sqlalchemy.orm import relationship
from backend.app import user
from backend.app.flight import BookingStatus, flight
from database.Session import Base


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
    
class User(Base):
     __tablename__="user"
    id = column(integer, primary_key=True, autoincrement = True)
    fullname = column(String(50))
    username=column(String(50))
    password= column(String(50))   
    
    
    
class Booking(Base):
     __tablename__="booking"
    id = column(integer, primary_key=True, autoincrement = True)
    status = column(BookingStatus)
    outboundFlight= column(flight)
    paymentToken= column(String(50)) 
    checkedIn= column(boolean) 
    customer= column(User) 
    createdAt= column(String(50)) 
    bookingReference= column(String(50)) 
    
#class bookingstatus(Base):
    
        
    
    