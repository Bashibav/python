# program to great a person which name starts with 's' in given list
lst=[]
for i in range(1,4):
    name=input(f"enter {i}st name: ")
    lst.append(name)
print("\n")
key=input("Enter the key to Great: ")
for name in lst:
    if(name.startswith(key)):
        print(f"Hello ! {name}, Welcome to Mahendrnager🙏")