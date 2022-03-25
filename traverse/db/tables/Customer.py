from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base

## One-to-One relationship
class Customer(Base):
    __tablename__ = "customer"
    
    id =  Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("customer", uselist=False))
    
    ## TODO: After creating package table
    payment = relationship("Customer", backref="payment")
    