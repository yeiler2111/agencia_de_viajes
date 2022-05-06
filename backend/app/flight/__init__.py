from logging import StreamHandler
from re import A
from tokenize import String
from typing_extensions import StrictTypeGuard
from unittest.mock import DEFAULT
from xmlrpc.client import Boolean
from xxlimited import Str
from enum import Enum

class flight(Base):
    
    id : int
    departuredate: Str
    departureAirportCode: str
    departureAirportName: Str
    departureCity: str
    departureLocale:str
    arrivalDate:str
    arrivalAirportCode:str
    arrivalAirportName:str
    arrivalCity:str
    arrivalLocale:str
    ticketPrice:int
    ticketCurrency:str
    flightNumber: int
    seatCapacity:int

"""class bookingStatus(str, int):
    CONFIRMED = 'CONFIRMED'
    UNCONFIRMED='UNCONFIRMED'
    CANCELLED='CANCELLED
    
"""
    
       
class User:
    id: int
    fullname: String
    username: String 
    password: String

class Booking:
    id: int
    status: BookingStatus
    outboundFlight: flight
    paymentToken: String
    checkedIn: Boolean
    customer: User
    createdAt: String
    bookingReference: String
    
