#program to create vector class and add method for add and multiply and print in 1i+4j+7k format using str function
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,other):
        result=vector(self.i+other.i,self.j+other.j,self.k+other.k)
        return result
    def __mul__(self,other):
        result=vector(self.i*other.i , self.j*other.j , self.k*other.k)
        return result
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
v11=int(input("Enter 'i' coff. of first cector: "))
v12=int(input("Enter 'j' coff. of first cector: "))
v13=int(input("Enter 'k' coff. of first cector: "))
v21=int(input("Enter 'i' coff. of second cector: "))
v22=int(input("Enter 'j' coff. of second cector: "))
v23=int(input("Enter 'k' coff. of second cector: "))
opt=input("Choose '+' for ADD and '*' for MUL: ")
vec1=vector(v11,v12,v13)
vec2=vector(v21,v22,v23)
if(opt=='+'):
    print(f"The sum of Vectors is {vec1+vec2}")
elif(opt=='*'):
    print(f"The product of Vectors is {vec1*vec2}")
else:
    print("Invalid operator!")