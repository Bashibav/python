#operator overloading is used to define what and how operator given id and do.
import os
import time
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
class number():
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def __add__(self):
        return self.n+self.m
    def __sub__(self):
        return self.n-self.m
    def __mul__(self):
        return self.n*self.m
    def __div__(self):
        return self.n/self.m
while True:
    clear_screen()
    print('''
choose your option
    + for sum
    - for diffrence
    * for multiplication
    / for division
''')
    n=int(input("enter first number: "))
    m=int(input("enter second number: "))
    op=input("choose operator: ")
    num=number(n,m)
    if(op== "+"):
         a=num.__add__()
         print(f"Sum = {a}")
    elif(op== "-"):
         b=num.__sub__()
         print(f"Difference = {b}")
    elif(op== "*"):
         c=num.__mul__()
         print(f"multiply = {c}")
    elif(op== "/"):
         d=num.__div__()
         print(f"division= {d}")
    else:
         print("Incorrect Option!")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
    time.sleep(0)
input("Press Enter to exit......")
