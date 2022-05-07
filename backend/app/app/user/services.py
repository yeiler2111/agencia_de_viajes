from typing import List, Optional
from . import models
from . import schema
from app.core import hashing
from app.booking import models as booking_models
from sqlalchemy.orm import Session



async def get_all_users(mydb_session: Session) -> List[models.User]:
    users = mydb_session.query(models.User).all()
    return users

async def get_user_by_id(user_id: int, mydb_session: Session) -> Optional[models.User]:
    user_info = mydb_session.query(models.User).get(user_id)
    return user_info

async def new_user_register(user_in: schema.UserCreate, mydb_session: Session) -> models.User:
    new_user = models.User(**user_in.dict())
    mydb_session.add(new_user)
    mydb_session.commit()
    mydb_session.refresh(new_user)
    return new_user

async def delete_user_by_id(user_id: int, mydb_session: Session):
    booking = mydb_session.query(booking_models.Booking).filter(booking_models.Booking.customer_id == user_id).all()
    if booking:
        for b in booking:
            mydb_session.delete(b)

    mydb_session.commit()
    mydb_session.query(models.User).filter(models.User.id == user_id).delete()
    mydb_session.commit()

async def update_user(user_id: int, user: schema.UserUpdate, mydb_session: Session):
    updated_user = models.User(**user.dict())
    mydb_session.query(models.User).filter(models.User.id == user_id).update(
                                            {
                                                models.User.id: user_id,
                                                models.User.fullname: updated_user.fullname,
                                                models.User.username: updated_user.username,
                                                models.User.password: updated_user.password
                                            }, synchronize_session=False)
    mydb_session.commit()
    return updated_user

def authenticate(*, username: str, password: str, mydb_session = Session) -> Optional[models.User]:
    user = mydb_session.query(models.User).filter(models.User.username == username).first()

    if not user:
        return None

    if not hashing.verify_password(password, user.password):
        return None
    
    return user