# lamda function
# Normally
'''def square(n):
    return n*n
n=int(input("Enter num: "))
print (f"The square of {n} is {square(n)}.")'''
# using lammda function
square= lambda n:n*n
n=int(input("Enter num: "))
print (f"The square of {n} is {square(n)}.")