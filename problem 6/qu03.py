# spam filters 
p1="make a lot of money"
p2="buy now"
p3="subscribe now"
p4="click this"

message =input("Enter your message: ")

if(p1 in message or p2 in message or p3 in message or p4 in message ):
    print("this is a spam comment")
else:
    print("not spam comment")
