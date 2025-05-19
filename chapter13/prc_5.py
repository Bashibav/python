#program to find max num using reduce
from functools import reduce
lst=[]
n=int (input("Enter number of item in list: "))
for i in range (n):
    num=int(input(f"Enter {i+1} num: "))
    lst.append(num)
print(lst)
def greater(a,b):
    if (a>b):
        return a
    return b
print(f" the greatest number is {reduce(greater,lst)}")