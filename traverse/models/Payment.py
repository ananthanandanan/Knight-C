

from Customer import Customer


class Payment():
    
    """Payment class"""
    
    def __init__(self, 
                payment_id,
                payment_mode,
                amount,
                status,
                time_stamp,
                customer:Customer) -> None:
        
        self.payment_id = payment_id
        self.payment_mode = payment_mode
        self.amount = amount
        self.status = status
        self.time_stamp = time_stamp
        ## Association-aggregation
        self.customer = customer
        
    def get_payment_id(self):
        return self.payment_id
    
    def get_payment(self):
        return [self.payment_mode, self.amount,
                self.status, self.time_stamp,
                self.customer.get_customer_id()]
        
        
        
        