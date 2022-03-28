from tables import (User, Employee, Customer, 
                    Admin, Manager, Agent,
                    Payment, Package,
                    Hotel, Ticket)
from tables.base import Base
import datetime
from Database import Database


dbms = Database("sqlite", dbname='travel.sqlite')
engine = dbms.db_engine

Base.metadata.create_all(engine)

# emp = Employee(id="1", designation="PR", doj=datetime.date(2018,7,12), user=User(id=1,name="Ananthan",dob=datetime.date(2000,8,9),
#                                                                     username="ank", Phno=123429323,
#                                                                     email="anank@gmail.com",
#                                                                     password="asdsads",
#                                                                     age=18))

# print(emp.user)
# session = dbms.session_manager()
# session.add(emp)
# session.commit()
# emp = session.query(Employee).all()
# for i in emp:
#     print("here",i.doj)

