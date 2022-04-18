
from Package import Package



class Hotel():
    """Hotel Class"""
    
    def __init__(self,
                hotel_id,
                hotel_name,
                status,
                location,
                hotel_cost) -> None:
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.status = status
        self.location = location # change field name
        self.hotel_cost = hotel_cost
        self.package_list = []
        
    def get_hotel_id(self):
        return self.hotel_id
    
    def get_hotel(self):
        return [self.hotel_name, self.hotel_name,
                self.status, self.location, self.hotel_cost]
        
    def add_package(self, package:Package):
        self.package_list.append(package)
        