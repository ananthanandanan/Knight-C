from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base
class Agent(Base):
    __tablename__ = "agent"
    
    id =  Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", backref=backref("agent", uselist=False))