# WAP to find the factorial of a num
n=int(input("enter the num : "))
  
if(n<0):
    print("fact not availble of nagative num")
else:
     i=1
     fact=1
     while(i<=n):
         fact *= i 
         i+=1
    
     print(fact)
        