from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base

class Manager(Base):
    __tablename__ = "manager"
    
    id =  Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey('employee.id', ondelete='CASCADE'), unique=True)
    employee = relationship("Employee", backref=backref("manager", uselist=False, passive_deletes=True))
    