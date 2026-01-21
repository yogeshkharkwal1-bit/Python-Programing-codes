class student:
    
    def __init__(self,name,roll_no,marks):
        self.name=name 
        self.__roll_no=roll_no #private--data mangling
        self._marks=marks
        if(roll_no<1):
            print("please enter the valid roll_no")
        if (name==""):
             print("enter the valid name")


    def get_name(self):
        return self.name 
        
    def set_roll_no(self,newroll_no):
        self.__roll_no=newroll_no

    def get_roll_no(self):
       return self.__roll_no  
      

std1=student("ram",5,355)     
print(f"name of a student is: {std1.name} \n its roll no is {std1._student__roll_no}\n and the total marks out of 500 is: {std1._marks}")   

std1.set_roll_no(0)
print("the new rollno is: ", std1.get_roll_no())


        







