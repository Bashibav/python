#methods used in list
lst=["nepal",55,"last","off","345.22"]
print(lst,"\n")
lst.append("cool") #adds new item at end of the list
print(lst)
#short method
num=[1,5,8,3,4,9,10,6]
num.sort()
print(num,"\n")

#reverse method
num.reverse()
print(num,"\n")

#insert method
lst.insert(2,"hello")
print(lst)

#pop method (return value at that index)
rm=lst.pop(4)
print(rm)
print(lst)
