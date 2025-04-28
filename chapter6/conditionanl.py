# conditional are used to execute program in certain condition only met requirement

a=int(input("enter your age: "))
if(a>=18):
    print(" You are eligible for voting.")
elif(a<=0):
    print("you entered invalid age number.")
else:
    print(" You are minor for voting.")