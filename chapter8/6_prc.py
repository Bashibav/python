#program to remove word from list and strip it at same time
lst=[]
for i in range(5):
    str=input("Enter item:")
    lst.append(str)
    i+=1

def rem(lst, word):
    n=[]
    for item in lst:
       if not(item==word):
        n.append(item.strip(word))
    return n

rm=input("Enter item to remove: ")
print(rem(lst,rm))