#program to find word from given txt find an sensor it with ####
words=["donkey","bad", "dirty","teeth"]
with open("para.txt") as f:
    para=f.read()
for word in words:
     para=para.replace(word,"#"*len(word))
with open("para.txt","w") as f:
    f.write(para)
with open("para.txt") as f:
    print(f.read())    