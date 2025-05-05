
#Program to make simple water, snake and gun game in python
'''
1 for water
-1 for snake
0 for gun
'''
import random
comp= random.choice([-1,1,0])
Youch=input("Enter your choice: ")
yourDict={"w":1, "s":-1, "g":0}
reveDict={1:"water", -1:"Snake", 0:"gun"}
you=yourDict[Youch]
print(f"You choose {reveDict[you]}\ncomputer choose {reveDict[comp]}")

if(comp== you):
    print("Its draw.")
else:
    if(comp==-1 and you==1):
        print("You lose!")
    elif(comp==-1 and you==0):
        print("You won!")
    elif(comp==1 and you==-1):
        print("You won!")
    elif(comp==1 and you==0):
        print("You lose!")
    elif(comp==0 and you==1):
        print("You won!")
    elif(comp==0 and you==-1):
        print("You lose!")
    else:
        print("something went wrong!")
