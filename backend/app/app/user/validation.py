from typing import Optional
from sqlalchemy.orm import Session
from . import models

async def verify_username_exist(username: str, mydb_session: Session) -> Optional[models.User]:
    return mydb_session.query(models.User).filter(models.User.username == username).first()

async def verify_fullname_exist(fullname: str, mydb_session: Session) -> Optional[models.User]:
    return mydb_session.query(models.User).filter(models.User.fullname == fullname).first()

async def verify_iduser_exist(user_id: int, mydb_session: Session) -> Optional[models.User]:
    return mydb_session.query(models.User).filter(models.User.id == user_id).first()