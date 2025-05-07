#progrma to find line number of the given word

with open("poem.txt") as p:
   print(p.read())
with open("poem.txt") as p:
   lines=p.readlines()
word=input("Enter word to find: ")
lineno=1
for line in lines:
    if (word in line):
         print(f"The word {word} is  present in {lineno} line.")
         break
    lineno +=1
else:
     print(f"The word {word} is not  present in poem.")