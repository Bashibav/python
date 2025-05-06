#use with statement instead of f.close()
#example
with open("file1.txt") as f:
    print(f.read())