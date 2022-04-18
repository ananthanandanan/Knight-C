from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base
class Agent(Base):
    __tablename__ = "agent"
    
    id =  Column(Integer, primary_key=True, index=True)
    emp_id = Column(Integer, ForeignKey('employee.id', ondelete='CASCADE'), unique=True)
    employee = relationship("Employee", backref=backref("agent", uselist=False, passive_deletes=True))
    packages = relationship("Package", backref=backref("agent", passive_deletes=True))