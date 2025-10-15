# wap to check the student is pass or fail 
name="suresh"
hindi = int(input("enter your hindi sub  num out of 100: "))
english = int(input("enter your english sub  num out of 100: "))
math= int(input("enter your math sub  num out of 100: "))
science = int(input("enter your science sub  numout of 100: "))

total =hindi+english+math+science
print("the total num gained by suresh is",total)

presentage=(total/400)*100
print("presentage are ",presentage)
print("\n")
if(presentage>=90):
    print("suresh is a brilient student ")
elif(presentage>=60 and presentage<90):
    print("suresh passed with 1st devision")
elif(presentage>=33 and presentage<60):
    print("suresh pass with 2nd devision") 
else:
    ("suresh failed")       

    