n=int(input("enter the num you check : "))
for i in range(2,n):
    if(n%i==0):
        print("the num is not prime")
        break
else:
    print("num is  prime")    