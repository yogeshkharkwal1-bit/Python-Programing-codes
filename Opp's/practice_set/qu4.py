class vehical:
    def __init__(self,brand,modal):
        self.brand=brand
        self.modal=modal

class car(vehical):
    def __init__(self,seats,engine,brand,modal):
        super().__init__(brand,modal) 
        self.seats=seats
        self.engine=engine


class bike(vehical):
    def __init__(self,seats,engine,brand,modal):
        super().__init__(brand,modal) 
        self.seats=seats
        self.engine=engine

car1=car("4seats","653cc","maruti","19s modal")    
bike1=bike("2seats","120cc","hero","20s modal")

print(car1.engine,car1.seats,car1.brand,car1.modal)
print(bike1.engine,bike1.seats,bike1.brand,bike1.modal)
# print(bike1.engine,bike1.seats)
