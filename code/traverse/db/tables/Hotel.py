from email.policy import default
from sqlalchemy import  Table, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, backref
from .base import Base

class Hotel(Base):
    
    __tablename__ = "hotel"
    
    id =  Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String(20), nullable=False)
    status = Column(String(30), nullable=False,default="available")
    location = Column(String(30), nullable=False)
    cost = Column(Float(precision=10, decimal_return_scale=None), nullable=False)
