# write a program to print a table with the help of for and whilw loop

x=int(input("enter the num : "))
for i in range (1,11):
    print(f"{x} X {i} = {x*i}")

x=int(input("enter the num : "))
i=1
while(i<11):
    print(f"{x} X {i} = {x*i}")
    i+=1
