#program to convert inches to centimeter
def cem(inc):
    return inc*2.54
inc=float(input("Enter in inches:"))
c=cem(inc)
print(f"The {inc} inches is equals to {round(c,2)} centemeters.")