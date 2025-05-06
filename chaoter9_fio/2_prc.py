# make a game()function to update players high-score
import random
def game():
    print("Your are playing the game ......")
    score=random.randint(1,100)
    #fetching the score
    with open("hi_score.txt") as f:
        hi_score= f.read()
        if(hi_score!=""):
            hi_score=int(hi_score)
        else:
            hi_score=0
    print(f"Your score: {score}")
    if(score>hi_score):
        with open("hi_score.txt","w") as f:
            f.write(str(score))
        return score
    else:
        return hi_score

d=game()
print(f"The highest score ever is {d}")
