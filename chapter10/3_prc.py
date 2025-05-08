#progrma to show booked train details
from random import randint
class train:
    def __init__(self,Ace,sleeper,general):
        self.Ace=Ace
        self.sleeper=sleeper
        self.general=general
    def book(self):
        Ace=12553
        sleeper=12443
        general=12332
    def getStatus(self):
        Ace="onetime"
        sleeper="30 min delay"
        general="15 min delay"
    def getfare():
        Ace=randint(500,3000)
        sleeper=randint(250,1500)
        general=randint(150, 1000)
    @staticmethod
    def greet():
        print("Welcome to Indian Railway 🙏")
while True:
    clear_screen()
    print('''
    Options:
      1. press 1 for Ace
      2. press 2 for Sleeper
      3. press 3 for General''')
    train.greet()
    opt=int(input("choose the option: "))
    name=input("Enter your name: ")
    b=train()
    if(opt==1):
