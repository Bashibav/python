#progbram to print multiplication table in reverse order using for loop
num=int(input("Enter Number: "))
for i in range(1,11):
    print(f"{num} X {11-i} = {num*(11-i)}")