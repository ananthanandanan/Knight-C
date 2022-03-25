from sqlalchemy import  (Column, Integer, String, ForeignKey, DateTime, Float)
from sqlalchemy.orm import relationship, backref
from .base import Base

class Payment(Base):
    __tablename__ = "payment"
    
    id =  Column(Integer, primary_key=True)
    mode = Column(String(10), nullable=False)
    amount = Column(Float(precision=10, decimal_return_scale=None), nullable=False)
    status = Column(String(10),nullable=False)
    timestamp = Column(DateTime, nullable=True)
    cust_id = Column(Integer, ForeignKey('customer.id'))