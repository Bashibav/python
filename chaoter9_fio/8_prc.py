#program to find if files are identical or not
with open("poem.txt") as p:
   new1=p.read()
with open("this_poem.txt") as p:
   new2=p.read()
if(new1==new2):
   print(" Files are Identical.")
else:
   print(" Files are not Identical.")