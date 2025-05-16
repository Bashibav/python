#exception handling 'raise'  keyword
num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
if(num2==0):
    raise ZeroDivisionError ("Devided by zero! invalid division.")
else:
    print(f" The division of {num1} by {num2} is {num1/num2}.")