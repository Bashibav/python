# program to guess corerect numaer and the person with minimum guess will win
import random
num=random.randint(1,100)
a=-1
guesses=1
while (a!=num):
    a= int(input("Guess The numaer: "))
    if (a>num):
       print(f"Guess the lower numaer please: ")
       guesses +=1
    elif(a<num):
        print(f"Guess the higher numaer please: ")
        guesses +=1
    else:
        print("correct!!!!")

print(f"You have guessed correctly {num} in {guesses} attempt.")