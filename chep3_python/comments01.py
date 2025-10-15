# today we learn the concepts of stringh

name="yogesh" # yogesh nmae is write in a string form

# we can not change the stringh becoz the string is mutable
# so we make a subh stringh for the given stringh 

lenght =len(name)  #stringh lenght is 0 to n-1 

print(lenght) #output is 6

 #we define the sub stringh with the strtingh or end index

nameshort=name[0:3]  # stringh with [0:5] here the 0 is strting index nand the 5 is end index

nameshort1=name[0:4] #4 not enclude

nameshort2=name[2:6]  #6 not enclude

print(nameshort)  # output is yog { only 0,1 and 2 index word write here 3-1 (n-1)}

print(nameshort1)# output is yoge { only 0,1,2 and 3 index word write here 4-1(n-1)}

print(nameshort2)# output is gesh{ only 2,3,4,5 index word write here 6-1 (n-1)}

#we also print a singhle charecter

char2=name[2]
print(char2) #output is [g]

# if we have not given the indx st or indx end that case 
nameshort3=name[0:]
print(nameshort3) #the end index= (n-1) automaticly by the inrterpreator

nameshort4=name[ :5]  #the st indx=0  automaticly by the inrterpreator
print(nameshort4)

a="kharkwal"
print(a[0:7:2]) #output is kaka becoz  first 0 idx=k next 2ns position char=a next 2nd.....=k, next.......=a
# the [2] i skip one letter and print the second letter to the word  
 
a="123456789"
print(a[1:7:3])   # out=25 idx1 to idx 7=1234567  1idx=2 and after 2 jumps 4rth idx val=5