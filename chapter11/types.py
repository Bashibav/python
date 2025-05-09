# types of inheritance
#multiple inheritance
class employee:# this base class called as parents class
    company="Microsoft"
    def __init__(self, name, sal):
        self.name=name
        self.sal=sal
    def show(self):
        print(f"{self.name} works in { self.company} with monthaly salary of {self.sal}" )
class coder:
    lang="python"
    def printlang(self):
        print(f"This is your language: {self.lang}")
class programmer(employee,coder):# using multiple inheritance
    company="Google"

name=input("Enter name: ")
sal=input("Enter ssalary: ")
a=employee(name,sal)
b=programmer(name,sal)
b.show()
b.printlang()