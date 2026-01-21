# create multiple funvtion with same name but it has dii=ffrebt form
# function overriding ....agr parent clas me koi function define ho or usi ki implementation child clas m bhi hui hoo us case ko function overrding khte he

class employee:
    def get_designation(self):
        print("designation=employee")

class teacher(employee):
    def get_designation(self):
        print("designation=teacher")  #function overriding
    
t1=teacher()
t1.get_designation()    

#DUCK TYPING  
# 1..esi classes jo ek dusre ke sath inherrir to nhi he but unke under ese fnction ki jarrrt he jo same work perform krta ho
# 2.. to un dono ko hum same name de skte he 



class teacher():
    def get_designation(self):
        print("designation=teacher")  


class accounts():
    def get_designation(self):
        print("designation=accounts")  

t1=teacher()
t1.get_designation()

acc1=accounts()
acc1.get_designation()