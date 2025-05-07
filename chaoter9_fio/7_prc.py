#program to copy files
with open("poem.txt") as p:
   new=p.read()
with open("this_poem.txt","w") as p:
    p.write(new)
  
with open("this_poem.txt") as p:
    print(p.read())