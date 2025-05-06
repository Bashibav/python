#append mode in file
st=input("Enter the data to write in file: ")
f=open("file1.txt","a")
f.write(st)

f=open("file1.txt")
line1=f.read()
print("\n",line1)
f.close()

