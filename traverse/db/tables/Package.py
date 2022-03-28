from tkinter.tix import Tree
from sqlalchemy import  Table, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, backref
from .base import Base


package_hotel = Table("package_hotel", Base.metadata,
        Column('pack_id', ForeignKey('package.id', ondelete="CASCADE"), primary_key=True),
        Column('hotel_id', ForeignKey('hotel.id', ondelete="CASCADE"), primary_key=True)
        )

class Package(Base):
        __tablename__ = "package"
        id =  Column(Integer, primary_key=True, index=True)
        name = Column(String(25), nullable=False)
        start_date = Column(Date, nullable=True)
        end_date = Column(Date, nullable=True)
        package_type = Column(String(10), nullable=True)
        cost = Column(Float(precision=10, decimal_return_scale=None), nullable=False)
        agent_id = Column(Integer, ForeignKey('agent.id',  ondelete='CASCADE'))
        ##one to many with ticket
        tickets = relationship("Ticket", backref=backref("package", passive_deletes=True))
        ##many to many with hotel
        hotels = relationship("Hotel",
                        secondary=package_hotel,
                        backref=backref("package", passive_deletes=True), 
                        cascade="all, delete")