from sqlalchemy import column, integer, String
from sqlalchemy.orm import relationship




class User(Base):
     __tablename__="user"
    id = column(integer, primary_key=True, autoincrement = True)
    fullname = column(String(50))
    username=column(String(50))
    password= column(String(50))   
    
    