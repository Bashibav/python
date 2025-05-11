#make a employee calss and add salry and increament property based on salary
class employee():
    def __init__(self,sal,inc):
        self.sal=sal
        self.inc=inc
    def grandTotal(self):
        print(f"The total salary is {self.totalsal}.\nThe bonus persent is {self.incPrc:.2f}%")
    @property
    def totalsal(self):
        return self.sal+self.inc
    @property
    def incPrc(self):
        return (self.inc/self.sal)*100
sal=float(input("Enter basic salary: "))
inc=float(input("Enter bonus ammount: "))
e=employee(sal,inc)
e.grandTotal()