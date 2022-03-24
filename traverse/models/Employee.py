from typing import List
from User import User

class Employee(User):
    
    """Employee Class"""
    def __init__(self, 
                user_id, 
                name, 
                dob, 
                Phno, 
                Address, 
                email, 
                username, 
                password, 
                age,
                employee_id,
                Designation,
                doj) -> None:
        super().__init__(user_id, 
                        name, 
                        dob, 
                        Phno, 
                        Address, 
                        email, 
                        username, 
                        password, 
                        age)
        self.employee_id = employee_id
        self.Designation = Designation
        self.doj = doj
        
    ## new method to be added to class diagram
    def get_emp_id(self):
        return self.employee_id
        
    ## New method from class diagram
    def get_Employee(self) -> List:
        
        return self.get_user() + [self.Designation, self.doj]