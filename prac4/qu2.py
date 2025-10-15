# accept 6 student marks and write in a sorted form

marks=[]
hindi=input("Enter here your Marks : ")
marks.append(hindi)

english=input("Enter here your Marks : ")
marks.append(english)

phy=input("Enter here your Marks : ")
marks.append(phy)

maths=input("Enter here your Marks : ")
marks.append(maths)

chem=input("Enter here your Marks : ")
marks.append(chem)


print("In hindi,english,phy,maths and chem - marks are:\n", marks)

marks.sort()
print("in sorted form the marks are\n",marks)