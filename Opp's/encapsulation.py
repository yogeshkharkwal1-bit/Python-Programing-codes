# wrapping data and functions into single unit 
# data + method = single unit(class)
"""
DATA HIDDING....
PUBLIC--data class ke under or behr dono jgh eccessable hota he
PRIVATE--bs class ke under use kr skte he
PROTECTED-- class or sub claass me use kr skte he
"""
class bankaccount:
    def __init__(self,name,department,balance):
        self.name=name #publivc
        self._department=department #protected
        self.__balance=balance #private--data mangling
    def get_balance(self):
        return self.__balance    

    def set_balance(self,newbalance):
        self.__balance=newbalancen

acc1=bankaccount("rohan","IT_SEC",60000)

print(acc1.name,acc1._department,)
"""
METHOD_1....isse hum privvate values ko acces kr skte he
print(acc1._bankaccount__balance) 
"""

# METHOD_2...we find the balance value by the funtions-getter and setter

acc1.set_balance(70000) #set the new balance value with the help of setter 
print(acc1.get_balance()) # get the new set ballance value 

print(acc1._bankaccount__balance)