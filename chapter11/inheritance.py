#inheritance is way of creating new class from existing class
class employee:# this base class called as parents class
    company="Microsoft"
    def __init__(self, name, sal):
        self.name=name
        self.sal=sal
    def show(self):
        print(f"{self.name} works { self.company} with monthaly salary of {self.sal}" )
class programmer(employee):# this is derived class also called child class of base class
    company="Google"

name=input("Enter name: ")
sal=input("Enter ssalary: ")
a=employee(name,sal)
print(a.show())
b=programmer(name,sal)
print(b.show())