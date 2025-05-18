# exception handling
try:
    num=int(input("Enter a number: "))
    print (f"You entered {num}.")
except Exception as e:
    print("you entered string. Please Enter number!")

