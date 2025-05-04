
#program to print greatest number among 3 numbers
def greatest(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c
a=int(input("Enter number 1st: "))
b=int(input("Enter number 2nd:"))
c=int(input("Enter number 3rd: "))
print(f"The greatest number is {greatest(a,b,c)}")