#program to print sum of first n natural numbers using recursive function
def sum(num):
    if (num==1):
        return 1
    return sum(num-1)+num
num=int(input("Enter the nth natural Number:"))
print(f"The sum of {num}th natural number is {sum(num)}.")