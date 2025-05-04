
#program to print following pattern using function
'''
***
**
*
'''
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
n=int(input("Enter the Number for pattern:"))
print(pattern(n))