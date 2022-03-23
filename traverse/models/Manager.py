
from models.Employee import Employee


class Manager(Employee):
    
    """Manager class"""
    
    def __init__(self, user_id, 
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
                doj,
                manager_id) -> None:
        
        super().__init__(user_id, 
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
                        doj)
        self.manager_id = manager_id
        
    ## new method for class diagram
    def get_manager_id(self):
        return self.manager_id
    def get_manager(self):
        return self.get_Employee() + [self.manager_id]