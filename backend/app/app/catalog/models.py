from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.user.models import User
from datetime import datetime
from app.database.db import Base
from app.catalog.models import Flight


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key = True, autoincrement = True)
    status = Column(String(40))
    outboundFlight_id = Column(Integer, ForeignKey(Flight.id, ondelete="CASCADE"))
    paymentToken = Column(String(100), default = '')
    checkedIn = Column(Boolean, default = False)
    customer_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"))
    createdAt = Column(DateTime, default = datetime.today())
    bookingReference = Column(String(40), unique = True)

    flight = relationship("Flight", back_populates="booking")
    customer = relationship("User", back_populates="booking")