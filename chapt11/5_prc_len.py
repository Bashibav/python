#program to create vector class and add method for add and multiply and print in 1i+4j+7k format using str function
class vector:
    def __init__(self,lst):
        self.i, self.j, self.k = lst
        self.lst=1
    def __add__(self,other):
        result=vector([self.i+other.i,self.j+other.j,self.k+other.k])
        return result
    def __mul__(self,other):
        result=vector([self.i*other.i , self.j*other.j , self.k*other.k])
        return result
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __len__(self):
        return len(self.lst)
lst1=[]
for i in range (3):
    num=int(input(f"Enter the coff. {['i', 'j', 'k'][i]} of first vector: "))
    lst1.append(num)
lst2=[]
for i in range (3):
    num=int(input(f"Enter the coff. {['i', 'j', 'k'][i]} of second vector: "))
    lst2.append(num)
opt=input("Enter '+' for ADD and '*' for Mul: ")
vec1=vector(lst1)
vec2=vector(lst2)
if(opt=='+'):
    print(f"The sum of Vectors is {vec1+vec2}")
elif(opt=='*'):
    print(f"The product of Vectors is {vec1*vec2}")
else:
    print("Invalid operator!")
print(f"The dimension of both Of vector is {len(vec1)}")