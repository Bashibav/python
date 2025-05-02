#program to print star opatter 
'''
*
**
***
'''
num=int(input("Number for pattern: "))
for i in range(1,num+1):
    print(" "*(num-1),end="")
    print("*"*i,end="")
    print(" ")