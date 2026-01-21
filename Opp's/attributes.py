"""bsasikly two types of attributes....

1st is class attributes jo class ke lie belong krta hai...
1..sttributes same honge kyuki sbhke lie availble he
2..example-- jese ek hi college me pdne vale student ka college name same hoga 
3...low priority becausew it is a common attributes
4..class or obj dono ke naam se print kr skte he

2nd is instance attributes jo object ke lie belong krta he.... 
1..unique ya different ho skte he kyuki har obj me alg values ho skti he 
2...example-- jese ek hi college me pdne vale student ka college name same hoga lekin uska khdu ka naam subject class alg alg hogi 
3...prioritty high rhti he
4..bs object ke naam se print kr skte he class name se error a jaeaga
"""


class student:
    college_name="apna college"
    PI=3.1

    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
        self.PI=3.14


std1=student("rahul",9)

#instance attributes 
print(f"{std1.name} cgpa is {std1.cgpa}") 


print(student.PI)

# print(student.college_name) get error because the name is a instance attributes 
print(student.college_name) #class attributes