#program to detect spam comments
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click here"

Message=input("Enter your cowmments:")

if((p1 in Message)or (p2 in Message) or (p3 in Message)or (p4 in Message)):
    print("This comment is spam!")
else:
    print("This isnot spam!")