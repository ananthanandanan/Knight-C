


from typing import List


class User(object):
    """User Class"""
    def __init__(self, 
                user_id, 
                name,
                dob,
                Phno,
                Address,
                email,
                username,
                password,
                age) -> None:
        
        self.user_id = user_id
        self.name = name
        self.dob = dob
        self.Phno = Phno
        self.Address = Address
        self.email = email
        self.username = username
        self.password = password
        self.age = age
    
    ## new method to be added to class diagram
    def get_user_id(self):
        return self.user_id
        
    def get_user(self) -> List:
        return [self.name, self.dob, 
                self.email, self.Phno, self.age,
                self.Address]
        
    def get_cred(self) -> List:
        return [self.username, self.password]
    
    def user_login(self, inp_name, inp_password):
        if (inp_name == self.username and 
            inp_password==self.password):
            return True
        return False
        
        