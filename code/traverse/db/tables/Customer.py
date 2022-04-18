from enum import unique
from sqlalchemy import  Table, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, backref
from .base import Base

customer_package = Table("customer_package", Base.metadata,
        Column('cus_id', ForeignKey('customer.id', ondelete='CASCADE'), primary_key=True),
        Column('pack_id', ForeignKey('package.id', ondelete='CASCADE'), primary_key=True)
        )

## One-to-One relationship -> user
## One to Many relationship -> payment
## Many to Many relationship -> package
class Customer(Base):
        __tablename__ = "customer"
        
        id =  Column(Integer, primary_key=True, index=True)
        ## when user is deleted then customer is also deleted.
        user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), unique=True)
        user = relationship("User", backref=backref("customer", uselist=False, passive_deletes=True))
        payments = relationship("Payment", backref=backref("customer", passive_deletes=True))
        packages = relationship("Package",
                                secondary=customer_package,
                                backref=backref("customer", passive_deletes=True),
                                cascade="all, delete")
