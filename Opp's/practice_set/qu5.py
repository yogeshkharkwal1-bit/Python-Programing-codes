
from abc import ABC,abstractmethod

class employee(ABC): #abstract class
    @abstractmethod
    #blue prints of its child class
    def calculate_selary(self): 
        pass
    
class intern(employee):
    def __init__(self,selary):
        self.selary=selary

    def calculate_selary(self): #implementation
        return self.selary


class fulltime(employee):
    def __init__(self,selary):
        self.selary=selary

    def calculate_selary(self): #implementation
        return self.selary


class contract(employee):

    def __init__(self,hour,per_hour):
        self.hour=hour
        self.per_hour=per_hour

    def calculate_selary(self): #implementation 
        return self.hour*self.per_hour   
        

intern1=intern(20000)
f1=fulltime(40000)
c1=contract(40,600)

print(intern1.selary)
print(f1.selary)
print(c1.calculate_selary())
        
