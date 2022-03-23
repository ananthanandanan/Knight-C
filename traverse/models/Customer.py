

from models.Package import Package
from typing import List
from models.User import User


class Customer(User):
    """Customer class"""
    
    def __init__(self, user_id, 
                name, 
                dob, 
                Phno, 
                Address, 
                email, 
                username, 
                password, 
                age,
                customer_id) -> None:
        super().__init__(user_id, 
                        name, 
                        dob, 
                        Phno, 
                        Address, 
                        email, 
                        username, 
                        password, 
                        age)
        self.customer_id = customer_id
        self.package_list = []
    
    ## New methods
    def get_customer_id(self):
        return self.customer_id
    
    def get_Customer(self) -> List:
        return self.get_user() + [self.customer_id]
    
    def add_package_list(self, package:Package):
        self.package_list.append(package)