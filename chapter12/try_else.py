# try with else clause
try:
    num=int(input("Enter a number: "))
    print (f"You entered {num}.")
except Exception as e:
    print("you entered string. Please Enter number!")
else: # only without error in try block executed, else block execute
    print("progrma inside above block executed successfully.")