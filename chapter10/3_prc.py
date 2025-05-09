#progrma to show booked train details
from random import randint
import os
import time
class train:
    def __init__(self,fro,to,name):
         self.fro=fro
         self.to=to
         self.name=name  
    def Ace(self):
        print(f"Welcome! {self.name} to Indian Railway Ace Coach.")
        print(f"Successfully! Booked ticket {self.fro} to {self.to}.\n Detials of your booking are:")
        print("The Train coach no. 12553. ")
        print(f"The total ticket ammount :{randint(500,3000)}")
        print(F"your train is{randint(5,10)} min. delay ")
    def Sleeper(self):
        print(f"Welcome {self.name} to Indian Railway Sleeper Coach.")
        print(f"Successfully! Booked ticket {self.fro} to {self.to}.\n Detials of your booking are:")
        print("The Train coach no. 12443. ")
        print(f"The total ticket ammount :{randint(200,1000)}")
        print(F"your train is{randint(10,20)} min. delay")
    def General(self):
        print(f"Welcome {self.name} to Indian Railway General  Coach.")
        print(f"Successfully! Booked ticket {self.fro} to {self.to}.\n Detials of your booking are:")
        print("The Train coach no. 12553. ")
        print(f"The total ticket ammount :{randint(100,300)}")
        print(F"Your train is {randint(5,10)} min. delay")
    @staticmethod
    def greet():
        print("Welcome to Indian Railway 🙏")
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
while True:
    clear_screen()
    train.greet()
    print('''
    Options:
      1. press 1 for Ace
      2. press 2 for Sleeper
      3. press 3 for General''')
    opt=int(input("choose the option: "))
    name=input("Enter your name: ")
    fro=input("Enter your boarding station: ")
    to=input("Enter your destination station: ")
    print("")
    b=train(fro,to,name)
    if(opt==1):
        print(b.Ace())
    elif(opt==2):
        print(b.Sleeper())
    else:
         print(b.General())
    choice= input("Do you want to book Again? (y/n)")
    if choice.lower()!="y":
         break
    time.sleep(0)
input("please, press enter to exit......")