# multilevel inheritance with using super key
class employe(): # super or base calss known as parent class
    company="Google"
    lang="Python"
    def __init__(self):
        self.name=name
        self.sal=sal
        self.name1=name1
    def emp(self):
        print(f"{name} is {self.lang} professional of {self.company} caompany.")
class position(employe): # inherits form employe class called as child class
    def position(self):
        print(f"{name} works as manager with monthly salary of {sal}.")
class intern(position):# inherits multilevel inheritence from position-->employe
    def __init__(self):
        self.name1=name1
        super().position() # using super key to call position method inside child intern
        super().emp()
    def hire(self):
        print(f"{name1} is hired as new intern at {self.company} by {name}.")
name="Toya"
sal=1245000
name1=input("enter the name of intern: ")
i=intern() # call by child class intern
i.hire()