from sqlalchemy import  Table, Column, Integer, String, ForeignKey, Date, Float, DateTime
from sqlalchemy.orm import relationship, backref
from .base import Base

class Ticket(Base):
    __tablename__ = "ticket"
    
    id =  Column(Integer, primary_key=True, index=True)
    froM = Column(String(20), nullable=False)
    to = Column(String(20), nullable=False)
    ticket_cost = Column(Float(precision=10, decimal_return_scale=None), nullable=False)
    arrival = Column(DateTime, nullable=False)
    departure = Column(DateTime, nullable=False)
    pack_id = Column(Integer, ForeignKey('package.id', ondelete='CASCADE'))
    