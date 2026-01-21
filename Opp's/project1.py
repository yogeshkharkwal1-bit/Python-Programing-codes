# design and create online store for products(name,prise) and also count the products
class product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price 
        product.count += 1

    def get_info(self):
        print(f"prise of {self.name} is {self.price}")
         
    @classmethod
    def get_count(cls):
        print(f"the total product in the store is: {cls.count} ") 

    @staticmethod
    def discount(price,diss):
        print(f"your new price of {price} is {price-(price*diss/100)}")
        print(f"you get the {(price*diss/100)}rs disscount  ")

p1=product("phone",10000)        
p2=product("leptop",100000)        
p3=product("tv",50000)        

product.get_count()
p1.discount(10000,12)