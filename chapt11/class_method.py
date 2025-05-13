#class method is way to directly acess a class inside method
# while giving object value instant value is priorely acessd over class value so @classmethod is used to access class value
class employ():
    company="Google"
    @classmethod #used to acess class value over instant value of given object.
    def emp(cls): # "cls" is used to acess class value.
        print(f"{name} work at {cls.company}")
name=input("Enter name: ")
emp=employ()
emp.company="Microsoft" #giving 'company' attribute instant value
emp.emp()