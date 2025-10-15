l1=[2,4,6,12,44,5,28,77,4,2,40,55]
l1.sort()
print(l1)  #the sort method change the list into aeesnding order [2, 4, 5, 6, 12, 28, 44]

l1.reverse()  #list ko reverse kr dega
print(l1)

l1.append(57) #list me 57 add kr dega
print(l1)

l1.pop(10)
print(l1)  #indx 10 vale value ko delt kr dega

l1.remove(77)
print(l1) 

l1.insert(3, 15) #index 3 me 15 add kr dega
print(l1)

print(l1.append(54)) #none
print(l1.pop(10)) #2
print(l1.insert(3,15)) #none
print(l1.remove(40))  #none