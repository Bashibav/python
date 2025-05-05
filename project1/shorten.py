
#Program to make simple water, snake and gun game in python
import os
import time
import random
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
comp= random.choice([-1,1,0])
while True:
    clear_screen()
    print('''
choose your option
w for water
s for snake
g for gun
''')
    Youch=input("Enter your choice: ")
    yourDict={"w":-1, "s":1, "g":0}
    reveDict={-1:"water", 1:"Snake", 0:"gun"}
    you=yourDict[Youch]
    print(f"You choose {reveDict[you]}\ncomputer choose {reveDict[comp]}")

    if(comp== you):
        print("Its draw.")
    else:
        if(comp-you==-1 or comp-you==2):
            print("You Lose!")
        elif(comp-you==1 or comp-you==-2):
            print("You Won!")
        else:
            print("something went wrong!")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != 'y':
        break
    time.sleep(0)
input("Press Enter to exit......")