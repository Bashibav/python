#program to find greatest numbers among four numbers giveb by user
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))
n4=int(input("Enter number 4:"))

if(n1>n2 and n1>n3 and n1>n4):
    print("The greatest numder is ",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("The greatest number is ",n2)
elif(n3>n2 and n3>n2 and n3>n4):
     print("The greatest number is ",n3)
else:
     print("The greatest number is ",n4)