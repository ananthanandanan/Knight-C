from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base

    
class Employee(Base):
    __tablename__ = "employee"
    
    id =  Column(Integer, primary_key=True)
    designation = Column(String(15), nullable=False)
    doj = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref=backref("employee", uselist=False))