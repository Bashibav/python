#program to make class programmerinfo to store information of programmers working at microsoft
class prog_info:
    company="Microsoft"
    def __init__(self,name,sal,pin):
        self.name=name
        self.sal=sal
        self.pin=pin
        print(f"the {name} of employee id no. {pin} has monthly salary {sal}")
name=input("Enter name of employee:")
sal=input("enter the salary:")
pin=input("enter pincode of employee:")
print(prog_info.company)
p=prog_info(name,sal,pin)
