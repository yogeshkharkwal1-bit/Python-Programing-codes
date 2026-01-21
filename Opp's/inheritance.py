# inheritance-- reusing the attributes and methods from a parent class 
"""                      emplpyee(base class)
        teacher(child class)                adminstry(child class) """

# this is the exp of single inheritance or multi inheritance 

class employee: #base class
    start_time="10 am"
    end_time="6pm"

class adminstry(employee): #child 1
    def __init__(self,role):
        self.role=role

    
class account(adminstry): #child2
    def __init__(self,tax,role): #role perameeter ko defineki jrurt nhi kyyuki inherit hui he class
        super().__init__(role) #ye basiikly role ko bhi input krne ke lie he jisse role ko bhi hum aces kr paenge
        self.tax = tax

e1=account("6%","manager") #tax and role input

print(e1.tax,e1.role) #calling the tax and role

#multiple inheritance example....
""" multiple parents but one child class

TEACHER CLASS              STUDENT CLASS
         
           CHILD_CLASS TA

"""
class teacher:
    def __init__(self,salary):
        self.salary=salary
         
class student:
    def __init__(self,cgpa):
        self.cgpa=cgpa

class TA(teacher,student):
    def __init__(self,salary,cgpa,name):
        super().__init__(salary) #we use the method for first class
        # super().__init__(cgpa) get error
        student.__init__(self,cgpa) #for inharrit 2nd parent class
        self.name=name

ta1=TA(15000,9.8,"yogi")
print(ta1.name,ta1.salary,ta1.cgpa)

