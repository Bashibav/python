# types of inheritance
#multilevel inheritance
class employee:# this base class called as parents class
    company="Microsoft"
    def __init__(self, name, sal):
        self.name=name
        self.sal=sal
    def show(self):
        print(f"{self.name} works in { self.company} with monthaly salary of {self.sal}" )
class programmer(employee):
    company="Google"
class intern(programmer):# creating multilevel inheritance
    company="Apple"
    name="Jenny"

name=input("Enter name: ")
sal=input("Enter ssalary: ")
a=employee(name,sal)
b=programmer(name,sal)
b.show()
c=intern(sal)
c.show()