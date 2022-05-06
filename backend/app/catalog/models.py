from lib2to3.pytree import Base
from sqlalchemy import column, integer, String, Boolean
from sqlalchemy.orm import relationship
from user.models import User


    
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
    
    

    