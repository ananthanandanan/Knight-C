from operator import index
from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base

    
class Employee(Base):
    __tablename__ = "employee"
    
    id =  Column(Integer, primary_key=True, index=True)
    designation = Column(String(15), nullable=False)
    doj = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), unique=True)
    user = relationship("User", backref=backref("employee", uselist=False, passive_deletes=True))