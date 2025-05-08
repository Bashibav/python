#make a calculator to calculate square, cube and root of given number
import os
import time
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        square= self.n*self.n
        print(f"The square of {self.n} is {square}")
    def cube(self):
        cube=self.n*self.n*self.n
        print(f"The cube of {self.n} is {cube}")
    def root(self):
        root=self.n**(1/2)
        print(f"The root of {self.n} is {root}")
    @staticmethod
    def greet():
        print("Hello, User! please choose the option.")
while True:
    clear_screen()
    print('''
    Options:
      1. to calculate square
      2. to calculate cube
      3. to calculate root''')
    calculator.greet()
    opt=int(input("choose the option: "))
    num=int(input("Enter the number: "))
    calc=calculator(num)
    if(opt==1):
        calc.square()
    elif(opt==2):
        calc.cube()
    else:
        calc.root()
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
    time.sleep(0)
input("Press Enter to exit......")