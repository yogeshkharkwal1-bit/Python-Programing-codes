name="yogesh" 

lenght =len(name) 
print(lenght)

nameshort=name[0:3]  
nameshort1=name[0:4]
nameshort2=name[2:6] 
nameshort3=name[0:]
nameshort4=name[ :5]
nameshort5=name[-5:-2]

print(nameshort) 
print(nameshort1)
print(nameshort2)
print(nameshort3)
print(nameshort4)
print(nameshort5)
 
# 2nd method to print the substring 

print(name[0:3]) 
print(name[0:4]) 
print(name[2:6]) 
print(name[0:]) 
print(name[:3]) 
print(name[:]) 
print(name[-4:-1])

#skip concepts of a string

a="123456789"
print(a[1:7:3])   # out=25 idx1 to idx 7=1234567  1idx=2 and after 2 jumps 4rth idx val=5
