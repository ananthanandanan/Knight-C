from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base
class Admin(Base):
    __tablename__ = "admin"
    
    id =  Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", backref=backref("admin", uselist=False))