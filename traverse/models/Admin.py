
from models.Employee import Employee


class Admin(Employee):
    
    """Admin class"""
    
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
                admin_id) -> None:
        
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
        self.admin_id = admin_id
        
    ## new method for class diagram
    def get_admin_id(self):
        return self.admin_id
    def get_agent(self):
        return self.get_Employee() + [self.admin_id]