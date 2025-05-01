#program to find factorial of given number using for loop
num=int(input("Enter the number to calculte factorial:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"The factorial of {num} is {fact}")
