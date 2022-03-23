from models.Agent import Agent
from models.Customer import Customer
from models.Hotel import Hotel
from models.Ticket import Ticket


class Package():
    """Package class"""
    
    def __init__(self,
                package_id,
                package_name,
                start_date,
                end_date,
                package_type,
                package_cost,
                agent: Agent) -> None:
        
        self.package_id = package_id
        self.package_name = package_name
        self.start_date = start_date
        self.end_date = end_date
        self.package_type = package_type
        self.package_cost = package_cost
        ## new field
        self.agent = agent
        self.customer_list = []
        self.hotel_list = []
        self.ticket_list = []
        
    def get_package_id(self):
        return self.package_id
    
    def get_package(self):
        
        return [self.package_name, self.package_cost,
                self.start_date, self.end_date,
                self.agent.get_agent_id()]
    ## new method for class diagram
    
    def add_paid_customer(self, customer:Customer):
        self.customer_list.append(customer)
    
    
    def add_hotel(self, hotel:Hotel):
        self.hotel_list.append(hotel)
        
    def add_ticket(self, ticket:Ticket):
        self.ticket_list.append(ticket)
    
        