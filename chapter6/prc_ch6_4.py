#program to find number of character in given user name
username=input("Enter user name: ")
if(len(username)<10):
    print("The username contains less than 10 character")
else:
    print("User name has more than 10 character.")