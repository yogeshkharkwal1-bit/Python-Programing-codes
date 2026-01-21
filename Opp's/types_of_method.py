class laptop:
    storage_type="ssd"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage 

    @classmethod
    # the only acces the class attributes
    def get_storage_type(cls):
        print(f"storage type= {cls.storage_type}")    

    def get_info(self): # instance info 
        print(f"leptop has {self.RAM} RAM and {self.storage}{self.storage_type}")    

    @staticmethod
    def cal_discount(prise,discount):
        final_prise=prise-(discount*prise/100)    
        print(f"final prise ={final_prise}")

l1=laptop("16gb","512gb")        

# print(laptop.get_storage_type())
l1.get_storage_type
l1.cal_discount(40000,10)



