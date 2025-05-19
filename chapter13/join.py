# join meethod
lst=[]
n=int (input("Enter number of item in list: "))
for i in range (n):
    str=input(f"Enter {i+1} item: ")
    lst.append(str)
print(lst)
s=input("Enter symbol to join: ")
final=s.join(lst)
print(final)
