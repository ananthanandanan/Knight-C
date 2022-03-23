
from models.Employee import Employee


class Agent(Employee):
    
    """Agent class"""
    
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
                agent_id) -> None:
        
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
        self.agent_id = agent_id
        
    ## new method for class diagram
    def get_agent_id(self):
        return self.agent_id
    def get_agent(self):
        return self.get_Employee() + [self.agent_id]