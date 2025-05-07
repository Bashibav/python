#program to find word from given txt find and replace it with ####
str=('''
     The average age of a donkey varies between 35 and 40 years.
 However, we know cases where donkeys have reached the age of 50.
You are able to determine how old a donkey is bad, by observing the teeth. 
Young donkeys have oval teeth. On growing older the teeth change from triangular to round.
 So, older donkeys have round teeth seen from above.
 A donkey becomes an adult when it is five. Only the stallion gets a wisdom tooth. dirty Old animals get “bags” on their eyes. 
The older the animal is, the deeper the pouches are.''')
with open("essay.txt","w") as f:
    f.write(str)
with open("essay.txt") as f:
    print(f.read())
word=input("Enter word to find: ")
with open("essay.txt") as f:
    essay=f.read()
    if (word in essay):
        rep_essay=essay.replace(word,"#####")
        print(rep_essay)