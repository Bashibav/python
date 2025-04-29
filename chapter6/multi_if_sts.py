a=int(input("Enter age:"))
#statement 1 start
if(a%2==0):
    print("Given age is even.")
else:
     print("given age is odd")
#statement 1 ends


#statement 2 start
if(a>=18):
    print(" You are eligible for voting.")
elif(a<=0):
    print("you entered invalid agee.")
else:
    print(" You are minor for voting.")
#statement 2 ends 
print(" program ends here." )