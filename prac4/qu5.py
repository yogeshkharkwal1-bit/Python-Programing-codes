# check given list is a palindrom or not....[1,2,3,2,1]
l1=[1,2,3,2,1]

l2=l1.copy()
l2.reverse()

if (l1==l2):
    print("given l1 is a palindrom")   
else:
      print("non palindrom")

c1=[1,2,3,4]
c2=c1.copy()
c2.reverse() 

if (c1==c2):
    print(" given c1 is a palindrom")   
else:
      print("given c1 is a non palindrom")