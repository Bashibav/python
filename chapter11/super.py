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
    def __init__(self, name, sal):
        self.name=name
        print(f"{self.name} is manager here.")
class intern(programmer):# creating multilevel inheritance
    company="Apple"
    name="jenny"
    print(f"{name} work as intern at {company}")
    def __init__(self, name, sal):
        super().__init__(name, sal)
name=input("Enter name: ")
sal=input("Enter ssalary: ")
a=employee(name,sal)
b=programmer(name,sal)
b.show()
c=intern(name,sal)
c.show()