#map filter reduce function
from functools import reduce
lst=[]
n=int (input("Enter number of item in list: "))
for i in range (n):
    num=int(input(f"Enter {i+1} num: "))
    lst.append(num)
print(lst)
square=lambda num:num*num
sqlst=map(square,lst)
print(list(sqlst))

#filter example
def even(num):
    if (num%2==0):
        return True
    return False
onlyeven=filter(even,lst)
print(list(onlyeven))

#reduce functionn
def sum(a,b):
    return a+b
print(reduce(sum,lst))