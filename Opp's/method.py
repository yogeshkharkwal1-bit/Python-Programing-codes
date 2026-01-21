# __init__method that also called constructor..
# that use to initilize our objects.

# har baar jese hi nai obj bnai jaegi ye method call hoga....or ye process automatic hoti he
# std1=stduent{}  yha per ye bracket ye  batate he hi init method ko call krdo.

# constructor 2 type k hote he perametreixe or default constructor 
"""
class student:
    def __init__(self):
        print("this is the constructor")

        # the self perameeter  is atomaticallly passede by the python

std1=student()"""

"""class student:
    def __init__(self,name,roll,cgpa):
        self.name=name
        self.roll=roll
        self.cgpa=cgpa

    def get_cgpa(self):
        return self.cgpa
        # self.name yani memory me her ek ke lie ek alg name create ho rha he islie self.name likha gya he  
        # the self perameeter  is atomaticallly passede by the python

std1=student("ram",32,8.6)
std2=student("syam",56,7)
std3=student("rohan",34,6)
std4=student("sohan",53,9)
 
print("std1 name is:  ",std1.name)
print("std2  rollno is : ",std2.roll)

print("the cgpa of std1 is:  ",std1.get_cgpa())
print("the cgpa of std2 is:  ",std2.get_cgpa())

print(f"{std1.name} has cgpa = {std1.get_cgpa()}")"""

class student:

    def __init__(self):
       print("example of default constructor")  #run nhi hoga kyuki multiple constructor allow nhi hote

    # ek class me ek hi consstructor use kr skkte he kyuki python ekhi constructor allow krta he..agr multiple he to last ko read kareag


    def __init__(self,name,roll,cgpa):  #perameeterized constructor
        self.name=name
        self.roll=roll
        self.cgpa=cgpa

    def get_cgpa(self):
        return self.cgpa


std1=student("ram",32,8.6)
std2=student("syam",56,7)
std3=student("rohan",34,6)
std4=student("sohan",53,9 )

print(f"{std1.name} has cgpa = {std1.get_cgpa()}")
