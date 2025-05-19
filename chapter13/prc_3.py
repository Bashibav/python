#program to convert list of multiplication table of number into verticle string
num=int(input("Enter number: "))
table=[str(num*i) for i in range(1,11)]
tab="\n".join(table)
print(tab)