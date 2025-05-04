#program to print multiples of given numbers using function
def multi(num):
    for i in range( 1, 11):
        print(f"{num} * {i} =  {num*i}")
num=int(input("Enter number to see multiples: "))
print(multi(num))