from Package import Package

class Ticket():
    
    def __init__(self,
                ticket_id,
                arrival,
                departure,
                From,
                To,
                ticket_cost) -> None:
        self.ticket_id = ticket_id
        self.arrival = arrival
        self.departure = departure
        self.From = From
        self.To = To
        self.ticket_cost = ticket_cost
        self.package_list = []
        
    def get_ticket_id(self):
        return self.ticket_id
    
    def add_package(self, package: Package):
        self.package_list.append(package)
    