#class to represent complex numbers with operator overloaded
class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)
    def __mul__(self,c2):
        real_part=self.r*c2.r-self.i*c2.i
        img_part=self.r*c2.i+self.i*c2.r
        return complex(real_part,img_part)
    def __str__(self):
        return f"{self.r} + {self.i}i"
n1=int(input("Enter real part of first complex num: "))
n2=int(input("Enter imaginary part of first complex num: "))
m1=int(input("Enter real part of second complex num: "))
m2=int(input("Enter imaginary part of second complex num: "))
c1=complex(n1,n2)
c2=complex(m1,m2)
print(f"The sum of given compex number is {c1+c2}")
print(f"The product of given compex number is {c1*c2}")
