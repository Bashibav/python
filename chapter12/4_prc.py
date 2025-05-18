#program to deviding num 1 bu=y num 2 which is zero
try:
    num1=int(input("Enter the number: "))
    num2=int(input("Enter the number: "))
    print(f"The quatant of {num1}/{num2} is {num1/num2}.")
except ZeroDivisionError as v:
    print("Infinite.")
   