#progam to filter listof numbers divisible by given number
lst=[]
n=int (input("Enter number of item in list: "))
for i in range (n):
    num=int(input(f"Enter {i+1} num: "))
    lst.append(num)
print(lst)
num1=int(input(f"Enter num to divide: "))
def div(num):
    if (num%num1==0):
        return True
    return False
divisible=filter(div,lst)
print(list(divisible))