
#recursion is function that repeatively calles itself

def fact(num):
    if (num==1 or num==0):
        return 1
    return num * fact(num-1)
num=int(input("Enter the number to see factorial: "))
print(f"The factorial of {num} is {fact(num)}.")