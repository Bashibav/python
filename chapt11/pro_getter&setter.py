# property decorator
# getter and setter method
class student:
    def details(self):
        print(f"The first name is {self.fname} and the last name is {self.lname}")
    @property #set the property as splitted part 
    def name(self,value):
        return f"{self.fname} {self.lname}"
    @name.setter #to set the values separatly splited from given string
    def name(self,value): 
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]
std=student()
std.name=input("Enter your full name: ")
std.details()
