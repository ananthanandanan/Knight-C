from email.mime import base
from enum import unique
from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from .base import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(30), nullable=False)
    dob = Column(Date, nullable=False)
    phno = Column(Integer, nullable=False)
    address = Column(String(50), nullable=True)
    email = Column(String(20), nullable=False, unique=True)
    username = Column(String(25), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    age = Column(Integer, nullable=False)
    
    def __repr__(self) -> str:
        return f"username={self.username} email={self.email} dob={self.dob}"
    