#readlines function used make list of lines
f=open("file1.txt")
#lines=f.readlines()
#print(lines,type(lines))
#readline fuction used to read line by line in given file
line1=f.readline()
while (line1!=""):
        print(line1)
        line1=f.readline()
f.close()

